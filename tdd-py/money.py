

class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    #def __add__(self, other):
    #    return Money(self.amount + other.amount, self.currency)

    def reduce(self, other):
        return 0

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def currency(self):
        return self.currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def euro(amount):
        return Money(amount, "EUR")

    def kiss(self):
        return 0
