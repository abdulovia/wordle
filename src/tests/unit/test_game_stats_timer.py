import unittest
import time
from game.game_engine import GameEngine


class TestGameTime(unittest.TestCase):

    def test_game_timer(self):
        game = GameEngine("melon", 1)

        wait_time = 3
        time.sleep(wait_time)
        game.play_turn("melon")

        stats = game.get_game_stats()

        self.assertGreater(stats["time_spent"], wait_time)


if __name__ == "__main__":
    unittest.main()
