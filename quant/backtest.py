from quant.portfolio import Portfolio
from quant.strategy import SMACrossoverStrategy
from matplotlib import pyplot as plt
import pandas as pd
import tempfile
import os

class BackTest():

    def __init__(self, portfolio, signals):
        self._portfolio = portfolio
        self._signals = signals
    
    def backtest(self):
        lot = 1
        pos = self._signals.fillna(0.0)
        pos['buy_sell_qty'] = lot*pos.signal
        pos['buy_sell_qty_value'] = lot*pos.signal*pos.Open
        pos['positions_carry_qty'] = pos.buy_sell_qty.cumsum().shift(1)
        pos['position_carry_val'] = pos.buy_sell_qty_value.cumsum().shift(1)
        pos['stock_value'] = (pos.buy_sell_qty + pos.positions_carry_qty)*pos.Close
        pos['cash'] = self._portfolio.cash - pos.position_carry_val - pos.buy_sell_qty_value
        pos['position_total'] = pos.stock_value + pos.cash
        pos['portfolio_returns'] = pos.position_total.pct_change()*100
        pos['mkt_returns'] = pos.Close.pct_change()*100
        return pos
    
    
p = Portfolio()
s = SMACrossoverStrategy(20,80)
signal = s.generateSignals('TCS',start_date="1995-01-01", end_date="2017-05-05")
t = BackTest(p, signal)
ret = t.backtest()
backtest_report = os.path.join(tempfile.gettempdir(),'backtest_tcs.csv')
print(backtest_report)
ret.to_csv(backtest_report)
plt.figure()
with pd.plot_params.use('x_compat', True):
    ret.sma_long.plot(color='r')
    ret.sma_short.plot(color='g')
plt.legend(loc='best')
plt.ioff()
plt.show()
