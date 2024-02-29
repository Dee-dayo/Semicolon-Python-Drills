from diary_app.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, diary_username: str, diary_password: str) -> None:
        diary = Diary(diary_username, diary_password)
        self.diaries.append(diary)

    def no_of_diaries(self) -> int:
        return len(self.diaries)

    def find_by_username(self, username: str) -> Diary:
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary

    def delete(self, diary_username: str, diary_password: str) -> None:
        for diary in self.diaries:
            if diary.get_username() == diary_username:
                self.diaries.remove(diary)
