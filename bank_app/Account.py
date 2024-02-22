from bank_app.invalid_amount_error import InvalidAmountError


class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        self.balance = self.balance + amount

    def check_balance(self, pin: str) -> int:
        if pin.isIncorrect():
            raise InvalidPinError("Pin is invalid")
        return self.balance

