
# abstract class for instruments in the Portfolio - Stocks, Bonds, Cash
from abc import ABCMeta, abstractmethod


class Instrument:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_instrument_details(self):
        raise NotImplementedError

    @abstractmethod
    def _transaction_cost(self, transaction):
        raise NotImplementedError

    @abstractmethod
    def get_current_value(self, transaction):
        raise NotImplementedError

    @abstractmethod
    def get_initial_transaction(self):
        raise NotImplementedError

    @abstractmethod
    def caculate_PnL(self):
        raise NotImplementedError

    @abstractmethod
    def get_current_price(self):
        raise NotImplementedError

    @abstractmethod
    def realized_pnl(self):
        raise NotImplementedError



