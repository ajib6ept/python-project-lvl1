import random

oper_functions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def generate_question():
    return (
        random.randint(1, 10),
        random.randint(1, 10),
        random.choice(("+", "-", "*")),
    )


def get_right_answer(question_num1, question_num2, question_oper):
    return str(oper_functions[question_oper](question_num1, question_num2))
