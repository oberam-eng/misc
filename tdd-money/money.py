

class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def kiss(self):
        return 0