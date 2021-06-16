import random


def get_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return get_gcd(a - b, b)
        else:
            return get_gcd(a, b - a)


def generate_question():
    return (random.randint(1, 40), random.randint(1, 40))


def get_right_answer(question_num1, question_num2):
    return str(get_gcd(question_num1, question_num2))
