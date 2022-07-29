import random
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_RANDOM_NUMBER = 10
MAX_RANDOM_NUMBER = 100


def is_prime_number(number):
    for num in range(2, int(sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def generate_question_and_answer():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    answer = "yes" if is_prime_number(question) else "no"
    return question, answer
