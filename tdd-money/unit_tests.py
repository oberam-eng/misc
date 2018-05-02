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

    def test_multiplication(self):
        self.assertEqual(Dollar(10), self.five.times(2))
        self.assertEqual(Dollar(15), self.five.times(3))

    def test_equality(self):
        self.assertEqual(Dollar(5), (Dollar(5)))
        self.assertNotEqual(Dollar(5), (Dollar(6)))


if __name__ == '__main__':
    unittest.main()
