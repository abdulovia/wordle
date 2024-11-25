import unittest
from db.database_manager import DatabaseManager
from game.game_engine import GameEngine


class TestDatabaseManager(unittest.TestCase):

    def test_database_manager(self):
        secret_word = "apple"
        attempts = 6
        game = GameEngine(secret_word, attempts)

        game.play_turn("party")
        game.play_turn("apple")  # correct guess

        # check game_stats correctness
        stats = game.get_game_stats()
        self.assertEqual(stats["attempts"], attempts - 1)
        self.assertEqual(stats["correct_guesses"], 1)
        self.assertGreater(stats["time_spent"], 0)

        # create a new database connection for test only
        db = DatabaseManager(db_name="test_database_manager.db")
        db.save_game_result(
            "Player1", stats["attempts"], stats["correct_guesses"], stats["time_spent"]
        )
        print("LOG INFO: inserted game_result in database: ", "Player1", stats["attempts"], stats["correct_guesses"], stats["time_spent"])

        results = db.fetch_all_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Player1")
        self.assertEqual(results[0][2], stats["attempts"])
        self.assertEqual(results[0][3], stats["correct_guesses"])
        self.assertEqual(results[0][4], stats["time_spent"])

        # drop test table
        db.drop_table()
