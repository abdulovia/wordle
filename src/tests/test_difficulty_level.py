import unittest
from game.word_picker import WordPicker
from game.difficulty_level import DifficultyLevel


class TestDifficultyLevelAndWordPicker(unittest.TestCase):

    def test_difficulty_level_and_word_picker(self):
        level = DifficultyLevel(level="hard")
        word_picker = WordPicker("resources/word_list.txt", level)
        word_picker.load_words()

        secret_word = word_picker.pick_secret_word()
        assert len(secret_word) == level.word_length
