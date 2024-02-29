from diary_app.diary import Diary


class MainApplication():
    def __init__(self):
        self.diary = Diary('Dee', 'my_password')

    def main_app(self):
        self.display_page()

    def display_page(self):
        print('''Welcome to Dee's Diary App
        1-> Create Diary
        2-> Find Diary
        3-> Unlock Diary
        4-> Add Entry
        5-> Lock Diary
        6-> Delete Entry
        7-> Find Entry
        8-> Update Entry
        9-> Exit App
        ''')


diary = MainApplication()
diary.main_app()