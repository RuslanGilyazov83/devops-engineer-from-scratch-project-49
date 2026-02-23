# -*- coding: utf-8 -*-
from brain_games import engine
from brain_games.games import gcd


def main():
    engine.run_game(gcd.DESCRIPTION, gcd.generate_round)


if __name__ == '__main__':
    main()