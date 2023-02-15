from random import choice, randint


game_rules = "What is the result of the expression?"


def get_question_with_answer():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    operation_sign = choice(("+", "-", "*"))
    if operation_sign == "+":
        answer = first_number + second_number
    elif operation_sign == "-":
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return f"{first_number} {operation_sign} {second_number}", str(answer)
