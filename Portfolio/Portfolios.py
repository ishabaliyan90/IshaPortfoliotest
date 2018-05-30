class Portfolio(object):
    def __init__(self, instrument_list, inst_type):
        self._instrumentList = instrument_list
        self.portfolioType = inst_type
        self.Value = self._calculate_total_value()
        self.instrumentNameMap = self.get_name_map()
        self.portfolio_pnl = 0

    def get_instruments_objects(self):
        return self._instrumentList

    def get_name_map(self):
        # method returns Map of instrument name and instrument details
        instrument_name_map = {}
        for instrument in self._instrumentList:
            instrument_name_map[instrument.Instrument_Name] = instrument
        return instrument_name_map

    def get_type(self):
        # method to define type of portfolio - can be amended if multiple portfolios are required
        self.portfolioType

    def get_total_value_of_portfolio(self):
        # method to get value of portfolio
        return self.Value

    def _calculate_total_value(self):
        # private method to calculate the current value of portfolio
        total_value = 0
        for instrument in self._instrumentList:
            total_value = total_value + (instrument.get_current_price() * instrument.get_quantity())
        return total_value

    def set_instrument_list(self, instrument_list):
        # method to create list of instruments in the portfolio
        self._instrumentList = instrument_list
        self._calculate_TotalValue()

    def set_pnl(self, pnl):
        self.portfolio_pnl = pnl

    def execute_new_transaction_on_portfolio(self, list_of_transaction):
        # PnL on new portfolio is zero.
        # The method calculates the PnL on any future transactions made on the instruments in portfolio
        portfolio_pnl = 0
        for transaction in list_of_transaction:
            instrument = self.instrumentNameMap[transaction.get_instrument()]
            instrument.add_transaction(transaction)
            portfolio_pnl = portfolio_pnl + instrument.caculate_PnL(transaction)
        self.set_pnl(portfolio_pnl)









