import random


def generate_question():
    return random.randint(1, 1000)


def is_odd_number(num):
    return num % 2 == 1


def get_right_answer(num):
    return "no" if is_odd_number(num) else "yes"
