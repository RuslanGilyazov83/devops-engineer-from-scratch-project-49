import prompt


def run_game(description, generate_round):
    """
    Запускает игру.

    Args:
        description: Строка с описанием правил игры
        generate_round: Функция, которая генерирует один раунд
                       и возвращает (question, correct_answer)
    """
    from brain_games.cli import welcome_user

    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(description)

    correct_answers = 0
    total_questions = 3

    while correct_answers < total_questions:
        question, correct_answer = generate_round()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
