from diary_app.diaries import Diaries
from diary_app.invalidusernameerror import InvalidUsernameError
from diary_app.invalid_id_no_error import InvalidIdNoError


class MainApplication:
    def __init__(self):
        self.diaries = Diaries()

    def main_app(self):
        self.display_page()

    def display_page(self):
        print('''DIARIES APP
        1-> Create Diary
        2-> Find Diary
        3-> Unlock Diary
        4-> Add Entry
        5-> Delete Entry
        6-> Update Entry
        7-> Exit App
        ''')
        user_input = input("").strip()
        match user_input:
            case '1':
                self.create_diary()
            case '2':
                self.find_diary()
            case '3':
                self.unlock_diary()
            case '4':
                self.add_entry()
            case '5':
                self.delete_entry()
            case '6':
                self.update_entry()
            case '7':
                print("Goodbye")
                exit(0)
            case _:
                self.display_page()

    def update_entry(self):
        print("Enter into your diary to delete entry")
        username = input("Enter your username: ")
        password = input("Enter password: ")
        try:
            my_diary = self.diaries.find_by_username(username)
            my_diary.unlock_diary(password)
            entry_no = input("Enter entry number: ")
            title = input("Enter title: ")
            body = input("Enter body: ")
            my_diary.update_entry(entry_no, title, body)
            print("***Entry successfully updated!***")
        except InvalidUsernameError as e:
            print(e)
        except InvalidIdNoError as e:
            print(e)
        finally :
            self.display_page()

    def delete_entry(self):
        print("Enter into your diary to delete entry")
        username = input("Enter your username: ")
        password = input("Enter password: ")
        try:
            my_diary = self.diaries.find_by_username(username)
            my_diary.unlock_diary(password)
            entry_no = input("Enter entry number: ")
            my_diary.delete_entry(int(entry_no))
        except InvalidUsernameError as e:
            print(e)
        except InvalidIdNoError as e:
            print(e)
        finally:
            self.display_page()

    def add_entry(self):
        print("Enter into your diary to add entry")
        username = input("Enter your username: ")
        password = input("Enter password: ")
        try:
            my_diary = self.diaries.find_by_username(username)
            my_diary.unlock_diary(password)
            title = input("Enter your Entry title: ")
            body = input("Enter your Entry body: ")
            my_diary.create_entry(title, body)
            print(f'''***Entry added successfully***\nYour entry number is {my_diary.get_entry_no()}''')
        except InvalidUsernameError as e:
            print(e)
        except InvalidIdNoError as e:
            print(e)
        finally:
            self.display_page()

    def unlock_diary(self):
        option = input("Have you created a Diary?? (1) Y    (2) N ")
        if option == '1':
            print("Unlocking Diary")
            username = input("Enter your username: ")
            password = input("Enter password: ")
            try:
                my_diary = self.diaries.find_by_username(username)
                my_diary.unlock_diary(password)
                print("***Diary has been unlocked***")
            except InvalidUsernameError as e:
                print(e)
            except InvalidIdNoError as e:
                print(e)
            finally:
                self.display_page()

        if option == '2':
            self.create_diary()
        else:
            self.display_page()

    def find_diary(self):
        print("FIND A DIARY")
        username = input("Enter your username: ")
        try:
            found_diary = self.diaries.find_by_username(username)
            print(f'Welcome {found_diary.get_username()}')
        except InvalidUsernameError as e:
            print(e)
        finally:
            self.display_page()

    def create_diary(self):
        print("CREATE A DIARY")
        user_name = input("Enter your Username: ")
        password = input("Enter your password: ")
        self.diaries.add(user_name, password)
        print('***Diary created Successfully***')
        self.display_page()


diary = MainApplication()
diary.main_app()
