import random

DESCRIPTION = "What number is missing in the progression?"

ITEMS_COUNT = 10


def generate_question_and_answer():

    first_number = random.randint(1, 10)
    step = random.randint(1, 10)
    progression_list = [str(first_number + step * i) for i in range(10)]

    # pick a random element and replace it
    answer_index = random.randint(0, 9)
    answer = progression_list[answer_index]
    progression_list[answer_index] = ".."
    question = " ".join(progression_list)
    return question, answer
