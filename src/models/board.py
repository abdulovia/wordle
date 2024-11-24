class Board:
    def __init__(self, max_attempts):
        self.max_attempts = max_attempts
        self.board = []

    def check_guess(self, guess, secret_word):
        feedback = []
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback.append("G")  # Correct letter, correct position
            elif guess[i] in secret_word:
                feedback.append("Y")  # Correct letter, wrong position
            else:
                feedback.append("B")  # Incorrect letter
        return "".join(feedback)

    def update_board(self, guess, feedback):
        self.board.append((guess.upper(), feedback))

    def display(self):
        print("\nCurrent Board:")
        for guess, feedback in self.board:
            print(f"{guess} - {feedback}")

    def is_full(self):
        return len(self.board) >= self.max_attempts
