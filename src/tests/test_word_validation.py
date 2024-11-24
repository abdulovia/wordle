import unittest
from unittest.mock import patch
from game.game_engine import GameEngine
from game.word_picker import WordPicker
from validation.word_validator import WordValidator
from db.database_manager import DatabaseManager
from utils.file_utils import load_words


class TestFullGameFlowWithValidationAndDatabase(unittest.TestCase):

    def test_game_with_validation_and_db(self):
        word_list = ["apple", "brick", "grape"]
        with patch('utils.file_utils.load_words', return_value=word_list):
            word_picker = WordPicker("src/resources/word_list.txt", level="easy")
            word_picker.load_words()

        secret_word = word_picker.pick_secret_word()

        game = GameEngine(secret_word)
        
        validator = WordValidator()
        guess = "apple"
        
        if validator.validate_word(guess):
            feedback = game.play_turn(guess)
        
        self.assertEqual(feedback, "GGGGG")

        stats = game.get_game_stats()

        db = DatabaseManager()
        db.save_game_result("Alice", stats["attempts"], stats["correct_guesses"], stats["time_spent"])

        results = db.fetch_all_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Alice")

if __name__ == '__main__':
    unittest.main()
