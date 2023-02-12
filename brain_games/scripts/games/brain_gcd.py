from random import randint
from brain_games.logic_for_games import main_game_logic


def get_two_random_numbers():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    return f"{first_number} {second_number}"


def get_gcd(two_numbers):
    two_numbers = two_numbers.split()
    first_number, second_number = int(two_numbers[0]), int(two_numbers[1])
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return str(first_number + second_number)


def main():
    game_rules = "Find the greatest common divisor of given numbers."
    main_game_logic(game_rules, get_two_random_numbers, get_gcd)


if __name__ == "__main__":
    main()
