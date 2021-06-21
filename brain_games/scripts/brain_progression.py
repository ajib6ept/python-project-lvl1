#!/usr/bin/env python

import prompt

from ..cli import welcome_user
from ..games.progression_game import generate_question, get_right_answer


def main():
    username = welcome_user()
    print("What number is missing in the progression?")
    attempt = 1
    while attempt < 4:
        question = generate_question()
        print(f"Question: {question}")
        answer = prompt.string(prompt="Your answer: ")
        right_answer = get_right_answer(question)
        if answer != right_answer:
            print(
                f"'{answer}' is wrong answer ;(. \
                Correct answer was '{right_answer}'"
            )
            print(f"Let's try again, {username}!")
            exit()
        print("Correct!")
        attempt = attempt + 1
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
