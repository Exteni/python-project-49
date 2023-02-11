from random import choice, randint
from brain_games.logic_for_games import main_game_logic


def get_expression():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    operation_sign = choice(("+", "-", "*"))
    return f"{first_number} {operation_sign} {second_number}"


def get_answer_for_expression(expression):
    expression = expression.split()
    expression[0], expression[2] = int(expression[0]), int(expression[2])
    if expression[1] == "+":
        answer = expression[0] + expression[2]
    elif expression[1] == "-":
        answer = expression[0] - expression[2]
    else:
        answer = expression[0] * expression[2]
    return str(answer)


def main():
    game_rules = "What is the result of the expression?"
    main_game_logic(game_rules, get_expression, get_answer_for_expression)


if __name__ == "__main__":
    main()