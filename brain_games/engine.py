import prompt
from brain_games.cli import welcome_user


def run_game(game_module):

    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_module.DESCRIPTION)

    correct_answers = 0
    total_questions = 3

    while correct_answers < total_questions:
        question, correct_answer = game_module.generate_round()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
