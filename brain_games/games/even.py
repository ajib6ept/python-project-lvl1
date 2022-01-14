import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    question = random.randint(10, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer
