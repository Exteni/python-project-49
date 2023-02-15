from brain_games.cli import welcome_user


def main_game_logic(game):
    username = welcome_user()
    print(game.game_rules)
    for _ in range(3):
        question, answer = game.get_question_with_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
