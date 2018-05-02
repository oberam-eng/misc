import unittest
from money import *


class TestMultiplication(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.five = Money.dollar(5)
        self.five_eur = Money.euro(5)

    '''
    def setUp(self):
        self.five = Dollar(5)
    '''

    def test_multiplication(self):
        self.assertEqual(Money.dollar(10), self.five.times(2))
        self.assertEqual(Money.dollar(15), self.five.times(3))

    def test_euro_multiplication(self):
        self.assertEqual(Money.euro(10), self.five_eur.times(2))
        self.assertEqual(Money.euro(15), self.five_eur.times(3))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), (Money.dollar(5)))
        self.assertNotEqual(Money.dollar(5), (Money.dollar(6)))
        self.assertEqual(Money.euro(5), (Money.euro(5)))
        self.assertNotEqual(Money.euro(5), (Money.euro(6)))
        self.assertNotEqual(Money.euro(5), Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("EUR", Money.euro(1).currency)


if __name__ == '__main__':
    unittest.main()
