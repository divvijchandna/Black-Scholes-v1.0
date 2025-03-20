import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, stock_price, strike_price, risk_free_interest_rate, time_to_expiration, volatility):
        self.stock_price = stock_price
        self.strike_price = strike_price
        self.risk_free_interest_rate = risk_free_interest_rate
        self.time_to_expiration = time_to_expiration
        self.volatility = volatility

    def d1(self):
        numerator = (np.log(self.stock_price / self.strike_price) +
                     (self.risk_free_interest_rate + 0.5 * self.volatility ** 2) * self.time_to_expiration)
        denominator = self.volatility * np.sqrt(self.time_to_expiration)
        return numerator / denominator

    def d2(self):
        return self.d1() - self.volatility * np.sqrt(self.time_to_expiration)

    def call_option_price(self):
        term1 = self.stock_price * norm.cdf(self.d1())
        term2 = self.strike_price * np.exp(-self.risk_free_interest_rate * self.time_to_expiration) * norm.cdf(self.d2())
        return term1 - term2

    def put_option_price(self):
        term1 = self.strike_price * np.exp(-self.risk_free_interest_rate * self.time_to_expiration) * norm.cdf(-self.d2())
        term2 = self.stock_price * norm.cdf(-self.d1())
        return term1 - term2