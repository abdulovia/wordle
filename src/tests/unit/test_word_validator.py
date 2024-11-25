import unittest
from validation.word_validator import WordValidator


class TestWordValidator(unittest.TestCase):

    def test_word_validation(self):
        validator = WordValidator()

        self.assertTrue(validator.validate_word("apple"))
        self.assertFalse(validator.validate_word("abcd"))
        self.assertFalse(validator.validate_word(""))


if __name__ == "__main__":
    unittest.main()
