from brain_games.cli import welcome_user


def main_game_logic(game):
    username = welcome_user()
    print(game.game_rules)
    for _ in range(3):
        question = game.question_for_user()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        right_answer = game.right_answer(question)
        if user_answer == right_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
    