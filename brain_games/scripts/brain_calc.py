from brain_games import engine
from brain_games.games import calc


def main():
    engine.run_game(calc.DESCRIPTION, calc.generate_round)


if __name__ == "__main__":
    main()
