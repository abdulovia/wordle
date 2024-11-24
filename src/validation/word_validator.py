import requests


class WordValidator:
    def __init__(self):
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def validate(self, word):
        response = requests.get(f"{self.api_url}{word}")
        return response.status_code == 200
