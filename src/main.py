import random
from game.game_engine import GameEngine
from game.word_picker import WordPicker
from game.difficulty_level import DifficultyLevel


def main():
    level = random.choice(["easy", "medium", "hard"])
    difficulty_level = DifficultyLevel(level)
    word_picker = WordPicker("src/resources/word_list.txt", difficulty_level)
    word_picker.load_words()
    secret_word = word_picker.pick_secret_word()

    game_engine = GameEngine(secret_word, difficulty_level.attempts)
    game_engine.start_game()


if __name__ == "__main__":
    main()
