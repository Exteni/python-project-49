from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 100


def get_question_with_answer():
    random_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    answer = "yes"
    for i in range(2, random_number // 2):
        if random_number % i == 0:
            answer = "no"
            break
    return random_number, answer
