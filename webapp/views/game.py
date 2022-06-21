from .messages import WIN_MESSAGE, INT_ERRORE_MESSAGE, LEN_ERRORE_MESSAGE, RANGE_ERRORE_MESSAGE, UNIQUE_ERRORE_MESSAGE, \
    MISSED_MESSAGE, RESULT_MESSAGE
from .generate_numbers import generate_numbers


class Game:
    secret_numbers = generate_numbers(4)

    def __init__(self) -> None:
        self.numbers = None

    def validation(self, numbers):
        if len(numbers) != 4:
            return LEN_ERRORE_MESSAGE
        if len(numbers) != len(set(numbers)):
            return UNIQUE_ERRORE_MESSAGE
        for i in numbers:
            if i > 9 or i < 1:
                return RANGE_ERRORE_MESSAGE
        self.numbers = numbers

    def get_result(self):
        bulls = 0
        cows = 0
        for i in range(len(self.numbers)):
            if self.numbers[i] == self.secret_numbers[i]:
                bulls += 1
            elif self.numbers[i] in self.secret_numbers:
                cows += 1

        if bulls == 4:
            Game.secret_numbers = generate_numbers(4)
            return WIN_MESSAGE
        elif bulls or cows:
            return RESULT_MESSAGE.format(bulls=bulls, cows=cows)
        else:
            return MISSED_MESSAGE
