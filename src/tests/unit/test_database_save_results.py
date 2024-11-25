import unittest
from unittest.mock import patch
from game.game_engine import GameEngine
from db.database_manager import DatabaseManager

class TestDatabaseIntegration(unittest.TestCase):

    def test_save_results_to_database(self):
        game = GameEngine("apple", 1)
        db = DatabaseManager()
        
        game.play_turn("apple")
        stats = game.get_game_stats()
        with patch('db.database_manager.DatabaseManager.save_game_result') as mock_save:
            db.save_game_result("TestPlayer", stats["attempts"], stats["correct_guesses"], stats["time_spent"])
        
        mock_save.assert_called_once_with("TestPlayer", 1, 1, stats["time_spent"])

if __name__ == '__main__':
    unittest.main()
