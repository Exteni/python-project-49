from random import randint

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_for_user():
    minimum_number = 1
    maximum_number = 100
    return randint(minimum_number, maximum_number)


def answer_for_question(question_for_user):
    for i in range(2, question_for_user // 2):
        if question_for_user % i == 0:
            return "no"
    return "yes"
