import random

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MAX_START = 50
MAX_STEP = 10


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_round():
    start = random.randint(1, MAX_START)
    step = random.randint(1, MAX_STEP)
    length = PROGRESSION_LENGTH

    progression = generate_progression(start, step, length)

    # Выбираем случайный индекс для скрытия
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    # Заменяем скрытое число на ".."
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer
