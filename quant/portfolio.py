from collections import OrderedDict

class Portfolio(object):
    
    def __init__(self):
        '''
            Assumptions:
            - Portfolio's initial cash balance = 1lakh in 
            - Single Currency ie. Rs.
            - No transaction costs
            - No brokerages
            - Selling Short is allowed
        '''
        self._stocks = dict()
        self._cash_amt = 1000000
        self._portfolio_aat = self._cash_amt
        
    @property
    def stocks(self):
        return self._stocks
    @stocks.setter
    def stocks(self, key, value):
        self._stocks[key] = value

    @property
    def portfolio_value(self):
        return self._cash_amt + self._stocks_amt

    @property
    def cash(self):
        return self._cash_amt