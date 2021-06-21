import random

LENGTH = 10


def generate_progression():
    first_element = random.randint(1, 20)
    step = random.randint(1, 7)
    progression = [
        str(first_element + step * (10 - n)) for n in range(LENGTH, 0, -1)
    ]
    return progression


def generate_question():
    question_progresson = generate_progression()
    question_progresson[random.randint(1, 8)] = ".."
    return " ".join(question_progresson)


def get_right_answer(question_progresson):
    first_num = question_progresson.split(" .. ")[0].split(" ")[-1]
    second_num = question_progresson.split(" .. ")[1].split(" ")[0]
    return str(int((int(first_num) + int(second_num)) / 2))
