import unittest

from bank_app.Account import Account
from bank_app.invalid_amount_error import InvalidAmountError


class MyTestCase(unittest.TestCase):
    def test_account_can_deposit(self):
        account = Account('Dayo Akinyemi', '1234')
        account.deposit(5_000)
        self.assertEqual(5_000, account.check_balance('1234'))

    def test_account_cant_deposit_negative_amount(self):
        account = Account('Dayo Akinyemi', '1234')
        with self.assertRaises(InvalidAmountError):
            account.deposit(-5_000)

    def test_account_cant_check_balance_with_wrong_pin(self):
        account = Account('Dayo Akinyemi', '1234')
        account.deposit(5_000)
        with self.assertRaises(InvalidPinError):
            account.check_balance('1111')