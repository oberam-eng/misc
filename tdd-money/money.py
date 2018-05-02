

class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount

    def equals(self, other):
        return self.amount == other.amount

    def kiss(self):
        return 0