#!/usr/bin/env python

from random import randint

import prompt

from ..cli import welcome_user


def is_odd_number(num):
    return num % 2 == 1


def get_right_answer(num):
    return "no" if is_odd_number(num) else "yes"


def main():
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    attempt = 1
    while attempt < 4:
        question_num = randint(1, 1000)
        print(f"Question: {question_num}")
        answer = prompt.string(prompt="Your answer: ")
        right_answer = get_right_answer(question_num)
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
            print(f"Let's try again, {username}!")
            exit()
        print("Correct!")
        attempt = attempt + 1
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
