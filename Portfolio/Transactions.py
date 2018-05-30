class Transaction (object):
    # class to define associated transactions defining
    # sale/purchase_price, buy/sell, quantity, date_of_purchase/sale, instrument_type of each instrument
    def __init__(self, price, side, quantity, date, instrument=""):
        self.Price = price
        self.Side = side
        self.Quantity = quantity
        self.Date = date
        self.Instrument = instrument

    def get_price(self):
        # returns purchase_price/sale_price of transaction
        return self.Price

    def get_side(self):
        # returns buy/sell on each transaction
        return self.Side

    def get_quantity(self):
        # returns quantity of sale/purchase of each
        return self.Quantity

    def get_date(self):
        # returns date of sale/purchase
        return self.Date

    def get_instrument(self):
        # returns instrument type of transaction
        return self.Instrument
