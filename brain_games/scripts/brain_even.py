from brain_games.cli import welcome_user
from random import randint


def get_random_number():
    minimum_number = 1
    maximum_number = 100
    return randint(minimum_number, maximum_number)


def check_answer(user_answer, random_number):
    right_answer = "yes" if random_number % 2 == 0 else "no"
    if random_number % 2 == 0 and user_answer == "yes":
        return True
    elif random_number % 2 != 0 and user_answer == "no":
        return True
    else:
        return right_answer


def main():
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = get_random_number()
        print(f"Question: {random_number}")
        user_answer = input("Your answer: ")
        right_answer = check_answer(user_answer, random_number)
        if right_answer is True:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
