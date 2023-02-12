from random import randint
from brain_games.logic_for_games import main_game_logic


def get_progression():
    random_step = randint(1, 30)
    progression = [str(i * random_step) for i in range(1, 11)]
    progression[randint(0, 9)] = ".."
    return " ".join(progression)


def get_missing_number(progression):
    progression = progression.split()
    missing_number_index = progression.index("..")
    if missing_number_index > 1:
        step = int(progression[1]) - int(progression[0])
    else:
        length = len(progression)
        step = int(progression[length - 1]) - int(progression[length - 2])
    return str(step * (missing_number_index + 1))
    


def main():
    game_rules = "What number is missing in the progression?"
    main_game_logic(game_rules, get_progression, get_missing_number)


if __name__ == "__main__":
    main()
