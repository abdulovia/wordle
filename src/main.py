from game.game_engine import GameEngine
from game.word_picker import WordPicker


def main():
    word_picker = WordPicker("src/resources/word_list.txt")
    word_picker.load_words()
    secret_word = word_picker.pick_secret_word()

    game_engine = GameEngine(secret_word)
    game_engine.start_game()


if __name__ == "__main__":
    main()
