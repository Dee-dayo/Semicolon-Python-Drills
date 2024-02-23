import unittest

from bank_app.Bank import Bank
from bank_app.account_not_found_error import AccountNotFoundError
from bank_app.invalid_amount_error import InvalidAmountError
from bank_app.invalid_pin_error import InvalidPinError


class MyTestCase(unittest.TestCase):
    def test_bank_can_register_customer(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        self.assertEqual(1, uba.no_of_accounts())

    def test_ban_can_register_two_customers(self):
        uba = Bank('UBA')
        account = uba.register_customer('Dayo', 'Akinyemi', '1234')
        account2 = uba.register_customer('Moh', 'Baba', '2222')

        self.assertEqual(2, uba.no_of_accounts())
        self.assertEqual(1002, account.get_account_number())
        self.assertEqual(1003, account2.get_account_number())

    def test_bank_can_find_account_by_account_number(self):
        uba = Bank('UBA')
        account = uba.register_customer('Dayo', 'Akinyemi', '1234')
        self.assertEqual(account, uba.find_account(1002))

        account2 = uba.register_customer('Moh', 'Baba', '2222')
        self.assertEqual(account2, uba.find_account(1003))

    def test_bank_cant_find_account_if_account_number_not_correct(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        with self.assertRaises(AccountNotFoundError):
            uba.find_account(1032)

    def test_bank_can_deposit_and_check_balance_of_account(self):
        uba = Bank('UBA')
        account = uba.register_customer('Dayo', 'Akinyemi', '1234')
        uba.deposit(1002, 5_000)
        self.assertEqual(5_000, account.check_balance('1234'))

    def test_bank_cant_deposit_negative_amount(self):
        uba = Bank('UBA')
        account = uba.register_customer('Dayo', 'Akinyemi', '1234')
        with self. assertRaises(InvalidAmountError):
            uba.deposit(1002, -5_000)

    def test_bank_cant_check_balance_with_incorrect_pin(self):
        uba = Bank('UBA')
        account = uba.register_customer('Dayo', 'Akinyemi', '1234')
        uba.deposit(1002, 5_000)
        with self.assertRaises(InvalidPinError):
            uba.check_balance(1002, '122224')

    def test_bank_can_withdraw(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        uba.deposit(1002, 5_000)
        uba.withdraw(1002, 3_000, '1234')
        self.assertEqual(2_000, uba.check_balance(1002, '1234'))

    def test_bank_cant_withdraw_with_incorrect_pin(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        uba.deposit(1002, 5_000)
        with self.assertRaises(InvalidPinError):
            uba.withdraw(1002, 3_000, '123234')

    def test_bank_can_transfer_money(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        account2 = uba.register_customer('Moh', 'Baba', '2222')
        uba.deposit(1002, 5_000)

        uba.transfer(1002, 1003, 2_000, '1234')
        self.assertEqual(3_000, uba.check_balance(1002, '1234'))
        self.assertEqual(2_000, uba.check_balance(1003, '2222'))

    def test_bank_can_remove_registered_account(self):
        uba = Bank('UBA')
        uba.register_customer('Dayo', 'Akinyemi', '1234')
        self.assertEqual(1, uba.no_of_accounts())

        uba.remove_account(1002, '1234')
        self.assertEqual(0, uba.no_of_accounts())