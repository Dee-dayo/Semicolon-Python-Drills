from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.__balance = balance

    # override to string method
    def __str__(self):
        return f"Account Name: {self.name}, Balance: {self.__balance}"


a1 = Account("John", Decimal(-10000.00))
print(a1)
