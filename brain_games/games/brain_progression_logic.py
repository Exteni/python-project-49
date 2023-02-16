from random import randint


GAME_RULE = "What number is missing in the progression?"
MINIMUM_POSSIBLE_STEP = 1
MAXIMUM_POSSIBLE_STEP = 30


def get_question_with_answer():
    step_progression = randint(MINIMUM_POSSIBLE_STEP, MAXIMUM_POSSIBLE_STEP)
    progression = [str(i * step_progression) for i in range(1, 11)]
    missing_number_index = randint(0, 9)
    answer = progression[missing_number_index]
    progression[missing_number_index] = ".."
    return " ".join(progression), str(answer)
