import random


def generate_question():
    return random.randint(3, 100)


def get_right_answer(num):
    for i in range(2, num):
        if num % i == 0:
            return "no"
    return "yes"
