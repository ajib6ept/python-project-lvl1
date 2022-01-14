import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(num1, num2):
    # need a string to compare with the user's answer
    return str(math.gcd(num1, num2))


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = find_gcd(num1, num2)
    return question, answer
