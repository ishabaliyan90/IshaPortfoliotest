from Instruments import Instrument
import logging


class Stock (Instrument):
    def __init__(self, instrument_name, current_transaction):
        self.Instrument_Name = instrument_name
        self.Initial_Transaction = current_transaction
        self.AllTransaction = [current_transaction]
        self.available_quantity = self.get_quantity()
        self.future_action = self.set_future_action(self.available_quantity)

    def get_instrument_details(self):
        return self.Instrument_Name

    def _transaction_cost(self, transaction):
        # implement transaction cost on transactions to be used in PnL calculations
        return 5

    def get_current_value(self, transaction):
        # returns current value of the instrument in portfolio
        return transaction.get_quantity() * transaction.get_price()

    def get_initial_transaction(self):
        return self.Initial_Transaction

    def add_transaction(self, transaction):
        # the method adds new transactions made on Stocks in the portfolio.
        # The method makes sure short positions are not allowed by the system
        new_quantity = 0
        if transaction.get_side() == 'Sell':
            new_quantity = self.get_quantity() - transaction.get_quantity()
        if new_quantity >= 0 :
            self.AllTransaction.append(transaction)
            self.set_future_action(self.get_quantity())
        else:
            logging.error('Short positions are not allowed in the system')
            raise IOError

    def get_current_price(self):
        # get price from some API - hardcoding it to a specific value for the time being
        price = 10
        return price

    def caculate_PnL(self, transaction):
        # method to calculate PnL on each item in the portfolio
        PnL = (transaction.get_quantity() * (self.get_current_price() - transaction.get_price())) - self._transaction_cost(transaction)
        return PnL

    def get_quantity(self):
        # method to calculate and update quantity of instrument
        quantity = 0
        for transaction in self.AllTransaction :
            if (transaction.get_side()) == 'Buy':
                quantity = quantity + transaction.get_quantity()
            else:
                quantity = quantity - transaction.get_quantity()
        return quantity

    def realized_pnl(self):
        buy_side_value = 0
        sell_side_value = 0
        for transaction in self.AllTransaction:
            if (transaction.get_side()) == 'Buy':
                buy_side_value = buy_side_value + ((transaction.get_quantity() * transaction.get_price())
                                                   - self._transaction_cost(transaction))
            elif transaction.get_side() == 'Sell':
                sell_side_value = sell_side_value + ((transaction.get_quantity() * transaction.get_price())
                                                     - self._transaction_cost(transaction))
            else:
                raise IOError
        realized_pnl = buy_side_value - sell_side_value
        return realized_pnl

    @staticmethod
    def set_future_action(quantity):
        # implementing a mock strategy - can be changed based on requirements
        if quantity < 10:
            return 'Buy'
        else:
            return 'Sell'







