import unittest
from game.game_engine import GameEngine

class TestGameEngine(unittest.TestCase):

    def test_game_stats_calculation(self):
        game = GameEngine(secret_word="grape", attempts=5)
        
        game.play_turn("apple") # -1 attempt
        game.play_turn("grape")
        
        stats = game.get_game_stats()
        self.assertEqual(stats["attempts"], 4)
        self.assertEqual(stats["correct_guesses"], 1)

if __name__ == '__main__':
    unittest.main()
