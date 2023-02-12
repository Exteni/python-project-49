from random import randint
from brain_games.logic_for_games import main_game_logic


def get_random_number():
    minimum_number = 1
    maximum_number = 100
    return randint(minimum_number, maximum_number)


def prime_or_not(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return "no"
    return "yes"


def main():
    game_rules = 'Answer "yes" if given number is '
    game_rules += 'prime. Otherwise answer "no".'
    main_game_logic(game_rules, get_random_number, prime_or_not)


if __name__ == "__main__":
    main()
