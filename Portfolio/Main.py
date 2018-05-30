from Stocks import Stock
from Bonds import Bonds
from Cash import Cash
from Transactions import Transaction
import datetime
from Portfolios import Portfolio

all_instrument = {}


def main(transaction_history):
    # this method assumes the transaction history is sent in the form of a dictionary.
    # It processes the transaction history of each instrument and creates a portfolio based on it.
    for key, value in transaction_history.iteritems():
        for all_bonds, tran_history in value.iteritems():
            transaction = get_current_quantity(tran_history)
            if key == 'Stock':
                instrument = Stock(all_bonds, transaction)
            elif key == 'Bonds':
                instrument = Bonds(all_bonds, transaction)
            elif key == 'Cash':
                instrument = Cash(all_bonds, transaction)
            else:
                raise ValueError('Instrument not defined')
            all_instrument[all_bonds] = instrument
    return create_portfolio()


def get_transaction_history():
    # get all transaction history from some API
    return {}


def create_portfolio():
    # method to create portfolio based on current holding of instruments
    portfolio = Portfolio(all_instrument.values(), type(all_instrument.values()))
    return portfolio


def get_current_quantity(tran_history):
    # method to process quantity of holding of each instrument based on transaction history
    current_quantity = 0
    current_price = 0.0

    for transaction in tran_history:
        if transaction.get_side() == 'Buy':
            current_quantity = current_quantity + transaction.get_quantity()
            current_price = transaction.get_price()
        else:
            current_quantity = current_quantity - transaction.get_quantity()
    return Transaction(current_price, 'Buy', current_quantity, datetime.date.today())


if __name__ == '__main__':
    # Main will take transaction history to create portfolio which can be passed as an input parameter for the
    # purpose of this exercise we have hard coded the transaction history. and the system creates
    # one portfolio per transaction history

    transactions = [Transaction(15, "Buy", 100, "27/10/2018"), Transaction(30, "Buy", 50, "23/11/2018"),
                    Transaction(30, "Buy", 80, "10/03/2017")]

    transactions1 = [Transaction(20, "Sell", 100, "27/10/2018"),
                     Transaction(30, "Buy", 50, "27/10/2018"),
                     Transaction(30, "Buy", 80, "23/11/2018")]
    transactions2 = [Transaction(1, "Buy", 100, "21/12/2018")]

    tran_history = {
        "Stock": {
            "Stock A": transactions,
            "Stock B": transactions1,
            "Stock C": transactions1 + transactions
        },
        "Bonds": {
            "Bond A": transactions,
            "Bond B": transactions1,
            "Bond C": transactions1 + transactions
        },
        "Cash": {
            "Cash": transactions2
        }
    }
    main(transaction_history=tran_history)