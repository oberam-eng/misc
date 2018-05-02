import unittest
from money import Dollar


class TestMultiplication(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.five = Dollar(5)

    '''
    def setUp(self):
        self.five = Dollar(5)
    '''

    def test_five(self):
        ten = self.five.times(2)
        self.assertEqual(10, ten.amount)

    def test_times_three(self):
        fifteen = self.five.times(3)
        self.assertEqual(15, fifteen.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))


if __name__ == '__main__':
    unittest.main()
