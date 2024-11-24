from validation.word_validator import WordValidator
from models.board import Board
from game.game_stats import GameStats


class GameEngine:
    def __init__(self, secret_word, attempts):
        self.secret_word = secret_word
        self.board = Board(attempts)
        self.word_validator = WordValidator()
        self.game_stats = GameStats(attempts)

    def start_game(self):
        print("Welcome to Advanced Wordle!")

        while self.game_stats.attempts > 0:
            guess = (
                input(
                    f"Attempts left: {self.game_stats.attempts}. Enter your {len(self.secret_word)}-letter guess: "
                )
                .strip()
                .lower()
            )

            if len(guess) != len(self.secret_word):
                print(f"Your guess must be {len(self.secret_word)} letters long.")
                continue

            if not self.word_validator.validate(guess):
                print("Not a valid English word.")
                continue

            feedback = self.board.check_guess(guess, self.secret_word)
            self.board.update_board(guess, feedback)
            self.board.display()

            if guess == self.secret_word:
                self.game_stats.increment_correct_guesses()
                self.game_stats.set_time_spent()
                print("Congratulations! You've guessed the word!")
                break

            self.game_stats.decrement_attempts()

        if self.game_stats.attempts == 0:
            print(f"Game over. The secret word was {self.secret_word.upper()}.")

    def game_turn(self, guess):
        if len(guess) != len(self.secret_word):
            print(f"Your guess must be {len(self.secret_word)} letters long.")

        if not self.word_validator.validate(guess):
            print("Not a valid English word.")

        feedback = self.board.check_guess(guess, self.secret_word)
        self.board.update_board(guess, feedback)
        self.board.display()

        if guess == self.secret_word:
            self.game_stats.increment_correct_guesses()
            self.game_stats.set_time_spent()
            print("Congratulations! You've guessed the word!")

        self.game_stats.decrement_attempts()

        if self.game_stats.attempts == 0:
            print(f"Game over. The secret word was {self.secret_word.upper()}.")

    def get_game_stats(self):
        return self.game_stats.get_stats()
