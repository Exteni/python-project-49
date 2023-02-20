from random import choice, randint


GAME_RULE = "What is the result of the expression?"
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 50


def get_question_with_answer():
    first_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    second_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    sign = choice(("+", "-", "*"))
    answer = get_answer_for_expression(first_number, second_number, sign)
    return f"{first_number} {sign} {second_number}", str(answer)


def get_answer_for_expression(first_operand, second_operand, operation_sign):
    if operation_sign == "+":
        return first_operand + second_operand
    elif operation_sign == "-":
        return first_operand - second_operand
    elif operation_sign == "*":
        return first_operand * second_operand
