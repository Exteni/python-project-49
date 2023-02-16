from random import randint
from math import gcd


GAME_RULE = "Find the greatest common divisor of given numbers."
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 50


def get_question_with_answer():
    number1 = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    number2 = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    return f"{number1} {number2}", str(gcd(number1, number2))
