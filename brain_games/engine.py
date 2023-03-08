import prompt

ROUNDS_NUMBER = 3


def execute(game):
    user_name = prompt.string("May I have your name? ")
    print("Hello, %s!" % user_name)
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_NUMBER):
        question, answer = game.generate_question_and_answer()
        print("Question: %s" % question)
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print("Correct!")
        else:
            print(
                "'%s' is wrong answer ;(. Correct answer was '%s'."
                % (user_answer, answer)
            )
            print("Let's try again, %s!" % user_name)
            exit()
    print("Congratulations, %s!" % user_name)
