import time

class GameStats:
    def __init__(self, attempts):
        self.attempts = attempts
        self.correct_guesses = 0
        self.time_spent = 0
        self.start_time = time.time()

    def decrement_attempts(self):
        self.attempts -= 1

    def increment_correct_guesses(self):
        self.correct_guesses += 1

    def set_time_spent(self):
        self.time_spent = time.time() - self.start_time

    def get_stats(self):
        return {
            "attempts": self.attempts,
            "correct_guesses": self.correct_guesses,
            "time_spent": self.time_spent
        }
