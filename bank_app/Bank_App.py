from bank_app.account_not_found_error import AccountNotFoundError
from bank_app.invalid_amount_error import InvalidAmountError
from bank_app.invalid_pin_error import InvalidPinError
from bank_app.Bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank('UBA')

    def main_app(self):
        self.display_menu()

    def display_menu(self):
        print("""Welcome to UBA Bank App
        1-> Register Account
        2-> Deposit
        3-> Withdraw
        4-> Transfer
        5-> Check Balance
        6-> Exit App
        """)
        user_input = input("").strip()

        match user_input:
            case '1':
                self.register_acc()
            case '2':
                self.deposit()
            case '3':
                self.withdraw()
            case '4':
                self.transfer()
            case '5':
                self.check_balance()
            case '6':
                exit()
            case _:
                self.display_menu()

    def check_balance(self):
        print("BALANCE CHECKER")
        account_number = int(input("Enter account number: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.check_balance(account_number, pin)
            print(f"Your Balance is {self.bank.check_balance(account_number, pin)}")
        except InvalidPinError as e:
            print(e)
        except AccountNotFoundError as e:
            print(e)
        finally:
            self.display_menu()

    def transfer(self):
        print("TRANSFER MONEY")
        sender_number = int(input("Enter sender account number: "))
        receiver_number = int(input("Enter receiver account number: "))
        amount = int(input("Enter amount to transfer: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.transfer(sender_number, receiver_number, amount, pin)
            print("Amount transferred successfully***")
        except InvalidAmountError as e:
            print(e)
        except InvalidPinError as e:
            print(e)
        except AccountNotFoundError as e:
            print(e)
        finally:
            self.display_menu()

    def withdraw(self):
        print("WITHDRAW MONEY")
        acc_number = int(input("Enter Account Number: "))
        amount = int(input("Enter amount to withdraw: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(acc_number, amount, pin)
            print("***Amount withdrawn Successfully***")
        except InvalidAmountError as e:
            print(e)
        except InvalidPinError as e:
            print(e)
        except AccountNotFoundError as e:
            print(e)
        finally:
            self.display_menu()

    def deposit(self):
        print("DEPOSIT MONEY")
        acc_number = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))
        try:
            self.bank.deposit(acc_number, amount)
            print("Amount deposited Successfully***")
        except AccountNotFoundError as e:
            print(e)
        except InvalidAmountError as e:
            print(e)
        finally:
            self.display_menu()

    def register_acc(self):
        print("REGISTER ACCOUNT")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        pin = input("Enter your pin number: ")
        account = self.bank.register_customer(first_name, last_name, pin)
        print(f"""
        ***Account Registered Successfully***
        Your account details are: {account.get_account_number()}\n""")
        self.display_menu()


bank = BankApp()
bank.main_app()
