from brain_games import engine
from brain_games.games import progression


def main():
    engine.run_game(progression.DESCRIPTION, progression.generate_round)


if __name__ == "__main__":
    main()
