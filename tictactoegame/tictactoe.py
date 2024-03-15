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
        self.__game_over = False

    def get_board(self):
        return self.__board

    def no_of_players(self):
        return self.__players

    def play(self, row_number, column_number):
        if 1 <= row_number <= 3 and 1 <= column_number <= 3:
            if self.__board[row_number - 1][column_number - 1] == BoardElements.EMPTY:
                if self.current_player == 1:
                    self.__board[row_number - 1][column_number - 1] = BoardElements.X
                    self.current_player = 2
                else:
                    self.__board[row_number - 1][column_number - 1] = BoardElements.O
                    self.current_player = 1

                if self.check_winner() != 0:
                    self.__game_over = True
                else:
                    self.check_game_end()

            else:
                raise InvalidInputError('Position already filled')
        else:
            raise InvalidInputError('Board has only 3 rows and 3 columns')

    def is_game_end(self):
        return self.__game_over

    def check_game_end(self):
        for row in range(3):
            for col in range(3):
                if self.__board[row][col] == BoardElements.EMPTY:
                    return
        self.__game_over = True

    def check_winner(self):
        for row in range(3):
            if self.__board[row][0] == self.__board[row][1] == self.__board[row][2] == BoardElements.X:
                return 1
            elif self.__board[row][0] == self.__board[row][1] == self.__board[row][2] == BoardElements.O:
                return 2

        for col in range(3):
            if self.__board[0][col] == self.__board[1][col] == self.__board[2][col] == BoardElements.X:
                return 1
            elif self.__board[0][col] == self.__board[1][col] == self.__board[2][col] == BoardElements.O:
                return 2

        if (self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == BoardElements.X) or \
                (self.__board[0][2] == self.__board[1][1] == self.__board[2][0] == BoardElements.X):
            return 1
        elif (self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == BoardElements.O) or \
                (self.__board[0][2] == self.__board[1][1] == self.__board[2][0] == BoardElements.O):
            return 2

        return 0

    def print_board(self):
        for row in self.__board:
            row_str = []
            for element in row:
                if element == BoardElements.EMPTY:
                    row_str.append(' ')
                elif element == BoardElements.X:
                    row_str.append('X')
                elif element == BoardElements.O:
                    row_str.append('O')
            print(" | ".join(row_str))
            print("-" * 9)


def main():
    game = TicTacToe()
    print("TIC-TAC-TOE!!!")
    print("Player 1 is X and Player 2 is O")
    game.print_board()

    while not game.is_game_end():
        try:
            row = int(input("Enter row number between 1, 2 or 3: "))
            column = int(input("Enter column number between 1, 2 or 3: "))
            game.play(row, column)
            game.print_board()
            if game.check_winner() == 1:
                print("Player 1 wins!")
                break
            elif game.check_winner() == 2:
                print("Player 2 wins!")
                break
            elif game.is_game_end():
                print("It's a draw!")
        except (ValueError, InvalidInputError) as e:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
