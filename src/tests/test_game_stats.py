import unittest
from unittest.mock import patch
from game.game_engine import GameEngine
from game.word_picker import WordPicker
from utils.file_utils import load_words


class TestGameTimeAndAttemptsIntegration(unittest.TestCase):

    def test_game_time_and_attempts(self):
        word_list = ["apple", "brick", "grape"]
        with patch('utils.file_utils.load_words', return_value=word_list):
            word_picker = WordPicker("src/resources/word_list.txt", level="easy")
            word_picker.load_words()

        secret_word = word_picker.pick_secret_word()

        game = GameEngine(secret_word)

        game.play_turn("apple")
        game.play_turn("grape")

        stats = game.get_game_stats()

        self.assertEqual(stats["attempts"], 2)
        self.assertGreater(stats["time_spent"], 0)

if __name__ == '__main__':
    unittest.main()
