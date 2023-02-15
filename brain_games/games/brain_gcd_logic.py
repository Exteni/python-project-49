from random import randint
from math import gcd


game_rules = "Find the greatest common divisor of given numbers."


def get_question_with_answer():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    return f"{number1} {number2}", str(gcd(number1, number2))
