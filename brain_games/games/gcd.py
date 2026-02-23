import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def generate_round():
    num1 = random.randint(1, MAX_NUMBER)  # NOSONAR
    num2 = random.randint(1, MAX_NUMBER)  # NOSONAR

    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer
