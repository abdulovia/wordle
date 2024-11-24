import unittest
from unittest.mock import patch
from game.word_picker import WordPicker
from game.game_engine import GameEngine
from game.difficulty_level import DifficultyLevel


class TestWordleIntegration(unittest.TestCase):

    def test_game_flow_with_difficulty(self):
        word_list = ["apple", "apple"]
        level = DifficultyLevel(level="medium")
        with patch("utils.file_utils.load_words", return_value=word_list):
            word_picker = WordPicker("src/resources/word_list.txt", level)
            word_picker.load_words()

        self.assertEqual(len(word_picker.words), 5)
        secret_word = word_picker.pick_secret_word()
        self.assertIn(secret_word, word_picker.words)

        game = GameEngine(secret_word)

        game.game_turn("apple")
        self.assertEqual(game.board.board, ["GGGGG"])

        stats = game.get_game_stats()
        self.assertEqual(stats["attempts"], 1)
        self.assertEqual(stats["correct_guesses"], 1)


if __name__ == "__main__":
    unittest.main()
