from Instruments import Instrument
import logging


class Cash(Instrument):
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
        return 0

    def get_current_value(self, transaction):
        return None

    def get_initial_transaction(self):
        return self.Initial_Transaction

    def add_transaction(self, transaction):
        # the method adds new transactions made on Bonds in the portfolio.
        # The method makes sure short positions are not allowed by the system
        new_quantity = 0
        if transaction.get_side() == 'Sell':
            new_quantity = self.get_quantity() - transaction.get_quantity()
        if new_quantity >= 0:
            self.AllTransaction.append(transaction)
            self.set_future_action(self.get_quantity())
        else:
            logging.error('Short positions are not allowed in the system')

    def get_current_price(self):
        # get price from some API - hardcoding it to a specific value for the time being
        # method can be amended based on FX implementation
        # It is assumed that all transaction are based on USD so price will be 1.
        # If transaction is in EUR, this will contain price from FX implementation
        return 1

    def caculate_PnL(self, transaction):
        # method to calculate PnL on each item in the portfolio
        # can be implemented based on FX PnL
        # It is not understood how PnL calculation will work for USD/USD cash.
        # In cases of a different ccy cash quantity, PnL calculations will go here
        return 0

    def get_quantity(self):
        # method to calculate and update quantity of instrument
        quantity = 0
        for transaction in self.AllTransaction:
            if (transaction.get_side()) == 'Buy':
                quantity = quantity + transaction.get_quantity()
            else:
                quantity = quantity - transaction.get_quantity()
        return quantity

    def realized_pnl(self):
        # method to calculate PnL on each item in the portfolio
        # can be implemented based on FX PnL
        # It is not understood how PnL calculation will work for USD/USD cash.
        # In cases of a different ccy cash quantity, PnL calculations will go here
        return 0

    @staticmethod
    def set_future_action(quantity):
        # implementing a mock strategy - can be changed based on requirements
        if quantity < 10:
            return 'Buy'
        else:
            return 'Sell'



