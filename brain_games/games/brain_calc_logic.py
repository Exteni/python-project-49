from random import choice, randint


game_rules = "What is the result of the expression?"


def question_for_user():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    operation_sign = choice(("+", "-", "*"))
    return f"{first_number} {operation_sign} {second_number}"


def answer_for_question(question_for_user):
    expression = question_for_user.split()
    expression[0], expression[2] = int(expression[0]), int(expression[2])
    if expression[1] == "+":
        answer = expression[0] + expression[2]
    elif expression[1] == "-":
        answer = expression[0] - expression[2]
    else:
        answer = expression[0] * expression[2]
    return str(answer)
