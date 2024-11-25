import unittest
from game.game_engine import GameEngine
from game.word_picker import WordPicker
from game.difficulty_level import DifficultyLevel


class TestGameStatsAndEngine(unittest.TestCase):

    def test_game_stats_and_engine(self):
        """
        testing GameStats correctness by guessing the word with 0 attempts left
        """
        level = DifficultyLevel("easy")
        word_picker = WordPicker("resources/word_list.txt", level)
        word_picker.load_words()

        # number of words equals number of attempts
        word_picker.words = word_picker.words[: level.attempts + 1]

        last_word = word_picker.words[-1]
        secret_word = last_word

        game = GameEngine(secret_word, level.attempts)

        for word in word_picker.words:
            game.play_turn(word)

        stats = game.get_game_stats()

        # guessed the last word that we made secret_word
        self.assertEqual(stats["attempts"], 0)
        self.assertEqual(stats["correct_guesses"], 1)
        self.assertGreater(stats["time_spent"], 0)
