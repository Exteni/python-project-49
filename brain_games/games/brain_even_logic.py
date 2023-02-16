from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 50


def get_question_with_answer():
    random_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    return random_number, "yes" if random_number % 2 == 0 else "no"
