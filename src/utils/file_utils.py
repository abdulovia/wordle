def load_words(filename):
    with open(filename, "r") as file:
        return [word.strip() for word in file.readlines()]
