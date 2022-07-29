import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 10
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    answer = "yes" if is_even(question) else "no"
    return question, answer
