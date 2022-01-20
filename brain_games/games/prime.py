import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def generate_question_and_answer():
    question = random.randint(10, 100)
    answer = "yes" if is_prime_number(question) else "no"
    return question, answer
