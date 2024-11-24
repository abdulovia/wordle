class DifficultyLevel:
    def __init__(self, level):
        self.level = level
        if self.level == "easy":
            self.word_length = 4
            self.attempts = 4
        elif self.level == "medium":
            self.word_length = 5
            self.attempts = 6
        elif self.level == "hard":
            self.word_length = 6
            self.attempts = 8

    def get_level_settings(self):
        return {
            "word_length": self.word_length,
            "attempts": self.attempts
        }
