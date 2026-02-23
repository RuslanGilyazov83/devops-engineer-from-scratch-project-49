import random

import prompt

from brain_games.cli import welcome_user


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def get_correct_answer(number):
    """Возвращает правильный ответ для заданного числа."""
    return "yes" if is_even(number) else "no"


def main():
    """Запускает игру «Проверка на чётность»."""
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    total_questions = 3

    while correct_answers < total_questions:
        number = random.randint(1, 100)
        print(f"Question: {number}")

        user_answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(number)

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
