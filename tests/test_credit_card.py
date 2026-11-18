import unittest
from model.credit_card import CreditCard

class TestCreditCard(unittest.TestCase):
    def test_charge(self):
        c=CreditCard("John","Chase","1111",5000)
        self.assertTrue(c.charge(1000))

if __name__ == '__main__':
    unittest.main()
