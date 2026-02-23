import operator
import random

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 50
OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
]


def generate_round():
    num1 = random.randint(1, MAX_NUMBER)  # nosec
    num2 = random.randint(1, MAX_NUMBER)  # nosec
    symbol, operation = random.choice(OPERATIONS)  # nosec

    question = f'{num1} {symbol} {num2}'
    correct_answer = str(operation(num1, num2))

    return question, correct_answer
