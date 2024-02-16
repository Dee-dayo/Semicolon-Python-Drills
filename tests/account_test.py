import unittest

from Account.Account import Account


class MyTestCase(unittest.TestCase):
    def test_account_is_open_balance_zero(self):
        myaccount = Account()
        self.assertEqual(0, myaccount.get_balance())

    def test_user_can_deposit(self):
        myaccount = Account()
        myaccount.deposit(10_000)
        self.assertEqual(10_000, myaccount.get_balance())

    def test_user_can_deposit_twice(self):
        myaccount = Account()
        myaccount.deposit(10_000.00)
        myaccount.deposit(5_000)
        self.assertEqual(15_000, myaccount.get_balance())

    def test_user_cant_deposit_lesser_than_zero(self):
        myaccount = Account()
        myaccount.deposit(-10_000)
        self.assertEqual(0, myaccount.get_balance())

    def test_user_cant_withdraw(self):
        myaccount = Account()
        myaccount.deposit(5_000)
        myaccount.withdraw(2_000)
        self.assertEqual(3_000, myaccount.get_balance())

    def test_user_cant_withdraw_lesser_balance(self):
        myaccount = Account()
        myaccount.deposit(5_000)
        myaccount.withdraw(10_000)
        self.assertEqual(5_000, myaccount.get_balance())

    def test_user_cant_withdraw_lesser_than_zero(self):
        myaccount = Account()
        myaccount.deposit(1_000)
        myaccount.withdraw(-1_000)
        self.assertEqual(1_000, myaccount.get_balance())