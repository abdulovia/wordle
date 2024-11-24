import random
from utils.file_utils import load_words


class WordPicker:
    def __init__(self, word_file_path):
        self.word_file_path = word_file_path
        self.words = []

    def load_words(self):
        self.words = load_words(self.word_file_path)

    def pick_secret_word(self):
        return random.choice(self.words)
