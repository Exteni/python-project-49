from random import randint


game_rules = "Find the greatest common divisor of given numbers."


def question_for_user():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    return f"{first_number} {second_number}"


def answer_for_question(question_for_user):
    two_numbers = question_for_user.split()
    first_number, second_number = int(two_numbers[0]), int(two_numbers[1])
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return str(first_number + second_number)
