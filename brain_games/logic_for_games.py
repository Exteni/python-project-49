from brain_games.cli import welcome_user


def main_game_logic(game_rules, question_for_user, answer_for_question):
    username = welcome_user()
    print(game_rules)
    for _ in range(3):
        question = question_for_user()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        right_answer = answer_for_question(question)
        if user_answer == right_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
