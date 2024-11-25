import unittest
from unittest.mock import patch
from game.word_picker import WordPicker
from game.difficulty_level import DifficultyLevel

class TestWordPicker(unittest.TestCase):
    
    def test_word_selection_based_on_difficulty(self):
        level = DifficultyLevel("medium")
        word_picker = WordPicker("resources/word_list.txt", level)
        word_picker.words = ["apple", "bricks", "grapes", "melon", "cherry"]
            
        word_picker.load_words()
        selected_word = word_picker.pick_secret_word()
        
        self.assertIn(selected_word, word_picker.words)
        self.assertEqual(len(selected_word), level.word_length)

if __name__ == '__main__':
    unittest.main()
