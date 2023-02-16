from random import randint


GAME_RULE = "Find the greatest common divisor of given numbers."
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 50


def get_question_with_answer():
    first_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    second_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    answer = get_gcd(first_number, second_number)
    return f"{first_number} {second_number}", answer


def get_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return str(first_number + second_number)
