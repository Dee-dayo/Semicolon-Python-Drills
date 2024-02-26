from diary.entry import Entry
from diary.invalid_id_no_error import InvalidIdNoError


class Diary:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__entries = []
        self.__entry_id = 1

    def is_locked(self) -> bool:
        return self.__is_locked

    def unlock_diary(self, password: str) -> None:
        if self.__password == password:
            self.__is_locked = False

    def lock_diary(self) -> None:
        self.__is_locked = True

    def create_entry(self, entry_title, entry_body) -> None:
        if not self.__is_locked:
            entry = Entry(self.__entry_id, entry_title, entry_body)
            self.__entries.append(entry)
            self.__entry_id += 1

    def no_of_entries(self) -> int:
        return len(self.__entries)

    def find_entry_by_id(self, id_no: int) -> Entry:
        for entry in self.__entries:
            if entry.id_no == id_no:
                return entry
        raise InvalidIdNoError('Invalid Id_No')

    def delete_entry(self, id_no: int) -> None:
        entry = self.find_entry_by_id(id_no)
        self.__entries.remove(entry)

    def update_entry(self, id_no, entry_title, entry_body):
        entry = self.find_entry_by_id(id_no)
        entry.title = entry_title
        entry.body = entry_body





