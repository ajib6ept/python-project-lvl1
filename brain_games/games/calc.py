import random

DESCRIPTION = "What is the result of the expression?"


FUNC = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def calculate_answer(num1, num2, operation):
    # need a string to compare with the user's answer
    return str(FUNC[operation](num1, num2))


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    question = f"{num1} {operation} {num2}"
    answer = calculate_answer(num1, num2, operation)
    return question, answer
