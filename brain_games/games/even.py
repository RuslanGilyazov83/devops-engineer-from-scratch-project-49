import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'


def generate_round():
    number = random.randint(1, MAX_NUMBER)  # nosec
    question = str(number)
    correct_answer = get_correct_answer(number)
    return question, correct_answer
