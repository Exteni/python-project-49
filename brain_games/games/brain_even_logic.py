from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 50


def get_question_with_answer():
    random_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    answer = get_even_or_not(random_number)
    return random_number, answer


def get_even_or_not(number):
    return "yes" if number % 2 == 0 else "no"
