

class Money:
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


class Dollar(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def kiss(self):
        return 0


class Euro(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def kiss(self):
        return 0
