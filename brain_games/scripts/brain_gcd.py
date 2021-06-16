#!/usr/bin/env python

import prompt

from ..cli import welcome_user
from ..games.gcd_game import generate_question, get_right_answer


def main():
    username = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    attempt = 1
    while attempt < 4:
        question_num1, question_num2 = generate_question()
        print(f"Question: {question_num1} {question_num2}")
        answer = prompt.string(prompt="Your answer: ")
        right_answer = get_right_answer(question_num1, question_num2)
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
