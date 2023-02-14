from random import randint


game_rules = "What number is missing in the progression?"


def question_for_user():
    step_progression = randint(1, 30)
    progression = [str(i * step_progression) for i in range(1, 11)]
    progression[randint(0, 9)] = ".."
    return " ".join(progression)


def answer_for_question(question_for_user):
    progression = question_for_user.split()
    missing_number_index = progression.index("..")
    if missing_number_index > 1:
        step = int(progression[1]) - int(progression[0])
    else:
        length = len(progression)
        step = int(progression[length - 1]) - int(progression[length - 2])
    return str(step * (missing_number_index + 1))
