import pandas as pd
from quant.portfolio import Portfolio
from quant.strategy import MarketData, SMACrossoverStrategy

class BackTest():
    
    def __init__(self, portfolio, signals):
        self._portfolio = portfolio
        self._signals = signals
        
    def backtest(self):
        lot = 1
        pos = self._signals.fillna(0.0)
        pos['position_qty'] = lot*pos.signal
        pos['position_change'] = pos.position_qty.diff()
        pos['position_value'] = pos.day_buy_sell*pos.Open
        pos['position_carry'] = self._portfolio.cash - (pos.position_change*pos.Open).cumsum()
        pos['position_total'] = pos.position_value + pos.position_carry
        pos['returns'] = pos.position_total.pct_change()
        return pos


p = Portfolio()
s = SMACrossoverStrategy(20,250)
signal1 = s.generateSignals('TCS')
signal2 = s.generateSignals('RELIANCE')
signals = pd.concat(signal1, signal2)
t = BackTest(p, signals)
t.backtest().to_csv('returns.csv')
