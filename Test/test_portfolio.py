import unittest
from Portfolio.Main import main as run
from Portfolio.Transactions import Transaction
from Portfolio.Portfolios import Portfolio as Portfolio
import datetime

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


class TestTransactionDetails(unittest.TestCase):

    def test_create_portfolio(self):
        profile = run(transaction_history=tran_history)
        assert type(profile) == Portfolio

    def test_portfolio_value(self):
        profile = run(transaction_history=tran_history)
        # with the above data - portfolio value calculates to be 10400
        self.assertEquals(profile.Value, 10500)

    def test_portfolio_PnL_when_portfolio_created(self):
        profile = run(transaction_history=tran_history)
        self.assertEquals(profile.portfolio_pnl, 0 )

    def test_allowed_to_trade_on_legal_limit(self):
        profile = run(transaction_history=tran_history)
        new_transaction = [Transaction(15, "Sell", 100, "27/10/2018", "Stock A")]
        profile.execute_new_transaction_on_portfolio(new_transaction)

    def test_short_position_is_allowed(self):
        #This is expected to fail IO Error
        profile = run(transaction_history=tran_history)
        new_transaction = [Transaction(15, "Sell", 300, "27/10/2018", "Stock A")]
        profile.execute_new_transaction_on_portfolio(new_transaction)


if __name__ == '__main__':
    unittest.main()


