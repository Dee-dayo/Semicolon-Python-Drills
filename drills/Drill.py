class Drill:
    def __init__(self):
        self.__word = ""

    def get_string(self):
        word = input("Enter a string: ")
        self.word = word.upper()

    def print_string(self):
        return self.word


drill = Drill()
drill.get_string()
print(drill.print_string())
