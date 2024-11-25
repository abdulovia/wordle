import unittest
from game.game_engine import GameEngine
from game.difficulty_level import DifficultyLevel
from validation.word_validator import WordValidator


class TestWordValidationAndEngine(unittest.TestCase):

    def test_word_validation_and_engine(self):
        """
        testing WordValidator by guessing word, that:
        1. does not exist in english dictionary
        2. exists in english dictionary
        """
        level = DifficultyLevel("medium")
        game = GameEngine(secret_word="apple", attempts=level.attempts)

        # invalid word guess attempt,
        result = game.play_turn("skdfj")
        self.assertEqual(result, "INCORRECT_WORD")

        # valid word guess attempt
        result = game.play_turn("words")
        self.assertEqual(result, "")

        # direct check with WordValidator
        validator = WordValidator()
        assert validator.validate("skdfj") == False, "word should not exist"
        assert validator.validate("words") == True, "word should exist"
