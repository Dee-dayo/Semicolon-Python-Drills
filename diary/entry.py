class Entry:
    def __init__(self, id_no: int, title: str, body: str):
        self.__title = title
        self.__body = body
        self.__id_no = id_no

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @property
    def id_no(self) -> int:
        return self.__id_no

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str) -> None:
        self.__body = body
