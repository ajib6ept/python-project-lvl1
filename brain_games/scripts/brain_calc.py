#!/usr/bin/env python

from random import choice, randint

import prompt

from ..cli import welcome_user
from ..games.calc_game import generate_question, get_right_answer


def main():
    username = welcome_user()
    print("What is the result of the expression?")
    attempt = 1
    while attempt < 4:
        question_num1, question_num2, question_oper = generate_question()
        print(f"Question: {question_num1} {question_oper} {question_num2}")
        answer = prompt.string(prompt="Your answer: ")
        right_answer = get_right_answer(question_num1, question_num2, question_oper)
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
            print(f"Let's try again, {username}!")
            exit()
        print("Correct!")
        attempt = attempt + 1
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
