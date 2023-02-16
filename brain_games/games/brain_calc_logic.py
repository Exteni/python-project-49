from random import choice, randint


GAME_RULE = "What is the result of the expression?"
MINIMUM_POSSIBLE_NUMBER = 1
MAXIMUM_POSSIBLE_NUMBER = 50


def get_question_with_answer():
    first_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    second_number = randint(MINIMUM_POSSIBLE_NUMBER, MAXIMUM_POSSIBLE_NUMBER)
    operation_sign = choice(("+", "-", "*"))
    if operation_sign == "+":
        answer = first_number + second_number
    elif operation_sign == "-":
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return f"{first_number} {operation_sign} {second_number}", str(answer)
