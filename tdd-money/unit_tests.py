import unittest
from money import *


class TestMultiplication(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.five = Dollar(5)
        self.five_eur = Euro(5)

    '''
    def setUp(self):
        self.five = Dollar(5)
    '''

    def test_multiplication(self):
        self.assertEqual(Dollar(10), self.five.times(2))
        self.assertEqual(Dollar(15), self.five.times(3))

    def test_euro_multiplication(self):
        self.assertEqual(Euro(10), self.five_eur.times(2))
        self.assertEqual(Euro(15), self.five_eur.times(3))

    def test_equality(self):
        self.assertEqual(Dollar(5), (Dollar(5)))
        self.assertNotEqual(Dollar(5), (Dollar(6)))
        self.assertEqual(Euro(5), (Euro(5)))
        self.assertNotEqual(Euro(5), (Euro(6)))


if __name__ == '__main__':
    unittest.main()
