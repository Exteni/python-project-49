from random import randint
from brain_games.game_logic import main_game_logic


def get_random_number():
    minimum_number = 1
    maximum_number = 100
    return randint(minimum_number, maximum_number)


def get_right_answer(question):
    return "yes" if question % 2 == 0 else "no"


def main():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    main_game_logic(game_rules, get_random_number, get_right_answer)


if __name__ == "__main__":
    main()
