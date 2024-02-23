from bank_app.Account import Account
from bank_app.account_not_found_error import AccountNotFoundError


class Bank(object):
    def __init__(self, name: str):
        self.name = name
        self.__accounts = []
        self.__account_number = 1002

    def register_customer(self, first_name: str, last_name: str, pin: str) -> object:
        account = Account(first_name + last_name, self.__account_number, pin)
        self.__accounts.append(account)
        self.__account_number += 1
        return account

    def no_of_accounts(self) -> int:
        return len(self.__accounts)

    def find_account(self, acc_no: int) -> object:
        for account in self.__accounts:
            if account.get_account_number() == acc_no:
                return account
        raise AccountNotFoundError("Account not found")

    def deposit(self, accNo: int, amount: int) -> None:
        account = self.find_account(accNo)
        account.is_invalid_amount(amount)
        account.deposit(amount)

    def check_balance(self, accNo: int, pin: str) -> int:
        account = self.find_account(accNo)
        account.is_correct_pin(pin)
        return account.check_balance(pin)

    def withdraw(self, acc_no: int, amount: int, pin: str) -> None:
        account = self.find_account(acc_no)
        account.is_invalid_amount(amount)
        account.is_correct_pin(pin)
        account.withdraw(amount, pin)

    def transfer(self, sender_acc_number: int, receiver_acc_number: int, amount: int, pin: str) -> None:
        sender_account = self.find_account(sender_acc_number)
        receiver_account = self.find_account(receiver_acc_number)
        sender_account.is_insufficient_fund(amount)
        sender_account.is_correct_pin(pin)

        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def remove_account(self, acc_no: int, pin: str) -> None:
        account = self.find_account(acc_no)
        account.is_correct_pin(pin)
        self.__accounts.remove(account)

