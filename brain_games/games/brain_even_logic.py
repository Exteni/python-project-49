from random import randint


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_for_user():
    minimum_number = 1
    maximum_number = 50
    return randint(minimum_number, maximum_number)


def answer_for_question(question_for_user):
    return "yes" if question_for_user % 2 == 0 else "no"
