from abc import ABCMeta, abstractmethod
import pandas as pd
import numpy as np
import quandl

class SMACrossoverStrategy():
    '''
        Return dataframe of signals: Generate buy, sell, hold signals: (1, -1 or 0) for each symbol
        Assumptions: 
            - Market orders
            - Market always fulfills generate signals
    '''
    def __init__(self, short_window=100, long_window=400):
        self._short_window = short_window
        self._long_window = long_window
    
    def generateSignals(self, stock):
            ts = MarketData.getTimeSeries(stock)
            signal = ts
            signal['signal'] = 0.0
            signal['sma_short'] = pd.rolling_mean(ts.Close, self._short_window, min_periods=1)
            signal['sma_long'] = pd.rolling_mean(ts.Close, self._long_window, min_periods=1)
            signal['signal'][self._short_window:] = np.where(   signal['sma_short'][self._short_window:] 
                                                             > signal['sma_long'][self._short_window:], 
                                                             1.0, 0.0
                                                            )
            ''' Take the difference of the signals in order to generate actual trading orders '''
            signal['positions'] = signal['signal'].diff()
            return signal
    
    @property
    def short_window(self):
        return self._short_window
    
    @property
    def long_window(self):
        return self._long_window
    
class MarketData:
    
    @classmethod
    def getTimeSeries(cls, stock, start_date="2000-01-01", end_date="2017-05-05"):
        exchg = 'NSE'
        ticker = exchg + '/' + stock
        df = quandl.get(ticker, start_date=start_date, end_date=end_date)
        df['Stock'] = stock
        df.rest_index()
        df.set_index(['Date','Stock'])
        df.sort_index(inplace=True)
        return df