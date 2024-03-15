import unittest

from tictactoegame.invalidinputerror import InvalidInputError
from tictactoegame.tictactoe import TicTacToe
from tictactoegame.tictactoe import BoardElements


class MyTestCase(unittest.TestCase):

    def test_game_has_3by3_board_filled_with_empty(self):
        game = TicTacToe()
        self.assertEqual(game.get_board()[0][0], BoardElements.EMPTY)

    def test_game_has_two_players(self):
        game = TicTacToe()
        self.assertEqual(game.no_of_players(), 2)

    def test_first_player_can_play_game(self):
        game = TicTacToe()
        game.play(1, 1)
        self.assertEqual(game.get_board()[0][0], BoardElements.X)

    def test_player_cant_play_invalid_row_or_column(self):
        game = TicTacToe()
        self.assertRaises(InvalidInputError, lambda: game.play(4, 5))

    def test_second_player_can_play_game(self):
        game = TicTacToe()
        game.play(1, 1)
        self.assertEqual(game.get_board()[0][0], BoardElements.X)

        game.play(2, 2)
        self.assertEqual(game.get_board()[1][1], BoardElements.O)

    def test_game_raise_error_if_position_already_occupied(self):
        game = TicTacToe()
        game.play(1, 1)
        self.assertEqual(game.get_board()[0][0], BoardElements.X)
        game.play(1, 2)
        self.assertEqual(game.get_board()[0][1], BoardElements.O)

        self.assertRaises(InvalidInputError, lambda: game.play(1, 1))

    def test_game_end_after_all_box_filled(self):
        game = TicTacToe()
        self.assertFalse(game.is_game_end())

        game.play(1, 1)
        game.play(1, 2)
        game.play(2, 2)
        game.play(1, 3)
        game.play(2, 3)
        game.play(2, 1)
        game.play(3, 1)
        game.play(3, 3)
        game.play(3, 2)

        self.assertTrue(game.is_game_end())

    def test_game_check_winner_when_game_ends(self):
        game = TicTacToe()
        game.play(1, 1)
        game.play(2, 1)
        game.play(3, 1)
        game.play(1, 2)
        game.play(2, 2)
        game.play(3, 2)
        game.play(1, 3)
        game.play(2, 3)
        game.play(3, 3)

        self.assertEqual(1, game.check_winner())

    def test_game_ends_winner_2_wins_game(self):
        game = TicTacToe()
        game.play(1, 1)
        game.play(1, 3)
        game.play(2, 1)
        game.play(2, 3)
        game.play(1, 2)
        game.play(3, 1)
        game.play(2, 2)
        game.play(3, 3)

        self.assertEqual(2, game.check_winner())

    def test_game_can_check_if_its_draw(self):
        game = TicTacToe()
        game.play(1, 1)
        game.play(1, 2)
        game.play(2, 2)
        game.play(1, 3)
        game.play(2, 3)
        game.play(2, 1)
        game.play(3, 1)
        game.play(3, 3)
        game.play(3, 2)

        self.assertEqual(0, game.check_winner())

    def test_ends_when_a_winner_is_already_gotten(self):
        game = TicTacToe()
        self.assertFalse(game.is_game_end())

        game.play(3, 1)
        game.play(2, 1)
        game.play(2, 2)
        game.play(1, 1)
        game.play(1, 3)

        self.assertEqual(1, game.check_winner())
        self.assertTrue(game.is_game_end())


if __name__ == '__main__':
    unittest.main()
