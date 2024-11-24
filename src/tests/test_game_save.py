import unittest
from unittest.mock import patch
from db.database_manager import DatabaseManager
from game.word_picker import WordPicker
from game.game_engine import GameEngine
from game.difficulty_level import DifficultyLevel
from utils.file_utils import load_words


class TestGameStatsAndDatabaseIntegration(unittest.TestCase):

    def test_game_stats_and_save_to_db(self):
        word_list = ["apple", "brick", "grape"]
        with patch('utils.file_utils.load_words', return_value=word_list):
            word_picker = WordPicker("src/resources/word_list.txt", level="hard")
            word_picker.load_words()

        secret_word = word_picker.pick_secret_word()

        game = GameEngine(secret_word)

        feedback = game.play_turn("apple")
        self.assertEqual(feedback, "BYYBB")

        stats = game.get_game_stats()

        self.assertEqual(stats["attempts"], 1)
        self.assertEqual(stats["correct_guesses"], 0)

        db = DatabaseManager()
        db.save_game_result("Alice", stats["attempts"], stats["correct_guesses"], stats["time_spent"])

        results = db.fetch_all_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Alice")
        self.assertEqual(results[0][2], stats["attempts"])

if __name__ == '__main__':
    unittest.main()
