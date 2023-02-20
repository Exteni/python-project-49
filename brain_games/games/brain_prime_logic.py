from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100


def get_question_with_answer():
    random_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    answer = prime_or_not(random_number)
    return random_number, answer


def prime_or_not(number):
    if number > 1:
        for i in range(2, number // 2):
            if number % i == 0:
                return "no"
        return "yes"
    else:
        return "no"
