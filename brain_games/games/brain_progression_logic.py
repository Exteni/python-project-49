from random import randint


GAME_RULE = "What number is missing in the progression?"
MINIMUM_POSSIBLE_STEP = 1
MAXIMUM_POSSIBLE_STEP = 30


def get_question_with_answer():
    progression = create_progression()
    answer = replace_random_number_with_dots(progression)
    return " ".join(progression), answer


def create_progression():
    step_progression = randint(MINIMUM_POSSIBLE_STEP, MAXIMUM_POSSIBLE_STEP)
    return [str(i * step_progression) for i in range(1, 11)]


def replace_random_number_with_dots(progression):
    index_of_number = randint(0, 9)
    number = progression[index_of_number]
    progression[index_of_number] = ".."
    return str(number)
