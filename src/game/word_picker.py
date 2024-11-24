import random
from utils.file_utils import load_words
from game.difficulty_level import DifficultyLevel


class WordPicker:
    def __init__(self, word_file_path, difficulty_level):
        self.word_file_path = word_file_path
        self.words = []
        self.difficulty_level = difficulty_level

    def load_words(self):
        self.words = load_words(self.word_file_path)
        level_settings = self.difficulty_level.get_level_settings()
        self.words = [
            word for word in self.words if len(word) == level_settings["word_length"]
        ]

    def pick_secret_word(self):
        return random.choice(self.words)
