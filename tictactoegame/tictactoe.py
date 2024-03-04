from tictactoegame.boardelements import BoardElements
from tictactoegame.invalidinputerror import InvalidInputError


class TicTacToe:

    def __init__(self):
        self.__board = [[BoardElements.EMPTY, BoardElements.EMPTY, BoardElements.EMPTY],
                      [BoardElements.EMPTY, BoardElements.EMPTY, BoardElements.EMPTY],
                      [BoardElements.EMPTY, BoardElements.EMPTY, BoardElements.EMPTY]
                      ]

        self.__players = 2
        self.current_player = 1

    def get_board(self):
        return self.__board

    def no_of_players(self):
        return self.__players

    def play(self, row_number, column_number):
        if 1 <= row_number <= 3 and 1 <= column_number <= 3:
            if self.__board[row_number][column_number] == BoardElements.EMPTY:
                if self.current_player == 1:
                    self.__board[row_number-1][column_number-1] = BoardElements.X
                    self.current_player = 2
                else:
                    self.__board[row_number-1][column_number-1] = BoardElements.O
                    self.current_player = 1

            else:
                raise InvalidInputError('Position already filled')
        else:
            raise InvalidInputError('Board has only 3 rows and 3 columns')



game = TicTacToe()
print(game.get_board())
