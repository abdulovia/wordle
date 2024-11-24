from validation.word_validator import WordValidator
from models.board import Board


class GameEngine:
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.attempts_left = 6
        self.board = Board(self.attempts_left)
        self.word_validator = WordValidator()

    def start_game(self):
        print("Welcome to Advanced Wordle!")

        while self.attempts_left > 0:
            guess = (
                input(
                    f"Attempts left: {self.attempts_left}. Enter your 5-letter guess: "
                )
                .strip()
                .lower()
            )

            if len(guess) != 5:
                print("Your guess must be 5 letters long.")
                continue

            if not self.word_validator.validate(guess):
                print("Not a valid English word.")
                continue

            feedback = self.board.check_guess(guess, self.secret_word)
            self.board.update_board(guess, feedback)
            self.board.display()

            if guess == self.secret_word:
                print("Congratulations! You've guessed the word!")
                break

            self.attempts_left -= 1

        if self.attempts_left == 0:
            print(f"Game over. The secret word was {self.secret_word}.")
