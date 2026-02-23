from brain_games import engine
from brain_games.games import even


def main():
    engine.run_game(even.DESCRIPTION, even.generate_round)


if __name__ == '__main__':
    main()
