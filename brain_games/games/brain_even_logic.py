from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_with_answer():
    minimum_number = 1
    maximum_number = 50
    random_number = randint(minimum_number, maximum_number)
    return random_number, "yes" if random_number % 2 == 0 else "no"
