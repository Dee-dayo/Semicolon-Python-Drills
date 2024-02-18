from problem import Type


class Problem:
    def __init__(self, name, type: Type):
        self.name = name
        self.type = type
        self.isSolved = False

    def check_status(self):
        return self.isSolved

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def change_status(self):
        self.isSolved = True
