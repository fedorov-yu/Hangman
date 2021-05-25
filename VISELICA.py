import random
from src.VISELICA.gameStatus import GameStatus


class InvalidOperationError(Exception):
    pass


class Game:
    def __init__(self, count_errors: int = 6):
        if count_errors < 5 or count_errors > 8:
            raise ValueError("count_errors must be should between 5 and 8")
        self.count_errors = count_errors
        self.current_list = []
        self.my_letters = []
        self.random_word = ''
        self.game_status = GameStatus.NOT_STARTED

    def set_letter(self, letter: str):
        if self.count_errors < 0:
            raise InvalidOperationError('Exceeded the max errors number')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f'Game status {self.game_status} ')

        self.my_letters.append(letter)
        for i, j in enumerate(self.random_word):
            if letter == j:
                self.current_list[i] = letter
        if letter not in self.random_word:
            self.count_errors -= 1
            print(f'{letter} not found, {self.count_errors} tries remaining')

        if self.random_word == "".join(self.current_list):
            self.game_status = GameStatus.WIN
        elif self.count_errors < 1 and self.random_word != "".join(self.current_list):
            self.game_status = GameStatus.LOSE

    def generate_word(self) -> str:
        filename = "../src/data/WordsStockRus.txt"
        with open(filename, encoding="utf-8") as word_file:
            self.random_word = random.choice(word_file.read().split())
        for _ in self.random_word:
            self.current_list.append('_')
        self.game_status = GameStatus.IN_PROGRESS
        #print(self.random_word) печатал разгадку, для проверки
        return "".join(self.current_list)

    def get_count_tries(self):
        return self.count_errors

    def get_current_string(self):
        return "".join(self.current_list)

    def get_my_letters(self):
        return "".join(sorted(self.my_letters))
