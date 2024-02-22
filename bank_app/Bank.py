from bank_app.Account import Account
from bank_app.account_not_found_error import AccountNotFoundError


class Bank(object):
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        self.account_number = 1002

    def register_customer(self, first_name: str, last_name: str, pin: str) -> object:
        account = Account(first_name + last_name, self.account_number, pin)
        self.accounts.append(account)
        self.account_number += 1
        return account

    def no_of_accounts(self) -> int:
        return len(self.accounts)

    def find_account(self, acc_no: int) -> object:
        for account in self.accounts:
            if account.get_account_number() == acc_no:
                return account
        raise AccountNotFoundError("Account not found")

    def deposit(self, accNo: int, amount: int) -> None:
        account = self.find_account(accNo)
        account.is_invalid_amount(amount)
        account.deposit(amount)

    def check_balance(self, accNo: int, pin: str):
        account = self.find_account(accNo)
        account.is_correct_pin(pin)
        return account.check_balance

    def withdraw(self, accNo: int, amount: int, pin: str):
        pass
