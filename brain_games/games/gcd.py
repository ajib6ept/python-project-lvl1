import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def find_gcd(num1, num2):
    # need a string to compare with the user's answer
    return str(math.gcd(num1, num2))


def generate_question_and_answer():
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f"{num1} {num2}"
    answer = find_gcd(num1, num2)
    return question, answer
