import unittest
from game.word_picker import WordPicker
from game.difficulty_level import DifficultyLevel


class TestDifficultyLevelAndWordPicker(unittest.TestCase):

    def test_difficulty_level_and_word_picker(self):
        for level in ["easy", "medium", "hard"]:
            difficulty_level = DifficultyLevel(level)
            word_picker = WordPicker("resources/word_list.txt", difficulty_level)
            word_picker.load_words()

            secret_word = word_picker.pick_secret_word()
            assert len(secret_word) == difficulty_level.word_length
