import unittest
from game.word_picker import WordPicker
from game.game_engine import GameEngine
from game.difficulty_level import DifficultyLevel


class TestGameBoardAndEngine(unittest.TestCase):

    def test_game_board_and_engine(self):
        level = DifficultyLevel(level="medium")
        word_picker = WordPicker("resources/word_list.txt", level)
        
        word = "blink"
        word_picker.words = [word]

        secret_word = word_picker.pick_secret_word()
        assert secret_word == word

        game = GameEngine(secret_word, level.attempts)

        guess_word = "brake"
        game.play_turn(guess_word)

        # check that board correctly returned letter placing
        # B L I N K – secret word
        # B R A K E – guess word
        # G B B Y B – board result
        self.assertEqual(game.board.board, [(guess_word.upper(), "GBBYB")])
