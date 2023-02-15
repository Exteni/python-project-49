from random import randint


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_with_answer():
    min_number = 1
    max_number = 100
    random_number = randint(min_number, max_number)
    answer = "yes"
    for i in range(2, random_number // 2):
        if random_number % i == 0:
            answer = "no"
            break
    return random_number, answer
