import unittest

from bank_app.Account import Account
from bank_app.insufficient_fund_error import InsufficientFundsError
from bank_app.invalid_amount_error import InvalidAmountError
from bank_app.invalid_pin_error import InvalidPinError


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

    def test_account_deposit_account_can_withdraw_money(self):
        account = Account('Dayo', '1234')
        account.deposit(5_000)
        account.withdraw(2_000, '1234')

    def test_account_depost_account_cant_withdraw_more_than_balance(self):
        account = Account('Dayo', '1234')
        account.deposit(5_000)
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(10_000, '1234')

    def test_account_depost_account_cant_withdraw_with_negative_amount(self):
        account = Account('Dayo', '1234')
        account.deposit(5_000)
        with self.assertRaises(InvalidAmountError):
            account.withdraw(-5000, '1234')

    def test_account_depost_account_cant_withdraw_with_invalid_pin(self):
        account = Account('Dayo', '1234')
        account.deposit(5_000)
        with self.assertRaises(InvalidPinError):
            account.withdraw(5000, '2222')

