from bank_app.insufficient_fund_error import InsufficientFundsError
from bank_app.invalid_amount_error import InvalidAmountError
from bank_app.invalid_pin_error import InvalidPinError


class Account:
    def __init__(self, name: str, number: int, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.number = number


    def deposit(self, amount: int):
        self.is_invalid_amount(amount)
        self.balance = self.balance + amount

    def is_invalid_amount(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")

    def check_balance(self, pin: str) -> int:
        self.is_correct_pin(pin)
        return self.balance

    def is_correct_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinError("Pin is invalid")

    def withdraw(self, amount: int, pin: str) -> None:
        self.is_insufficient_fund(amount)
        self.is_invalid_amount(amount)
        self.is_correct_pin(pin)
        self.balance = self.balance - amount

    def is_insufficient_fund(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient fund")

    def get_account_number(self):
        return self.number

