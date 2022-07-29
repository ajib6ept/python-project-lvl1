import random

DESCRIPTION = "What number is missing in the progression?"

ITEMS_COUNT = 10

MIN_ANSWER_ELEMENT = 0
MAX_ANSWER_ELEMENT = 0

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 10

PROGRESSION_LENGTH = 10


def create_progression(initial_term, common_difference, length):
    progression = [
        str(initial_term + common_difference * i) for i in range(length)
    ]
    return progression


def get_string_of_progression(progression, index):
    progression[index] = ".."
    return " ".join(progression)


def generate_question_and_answer():
    initial_term = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    common_difference = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    length = PROGRESSION_LENGTH
    progression_list = create_progression(
        initial_term=initial_term,
        common_difference=common_difference,
        length=length,
    )

    # pick a random element and replace it
    answer_index = random.randint(MIN_ANSWER_ELEMENT, MAX_ANSWER_ELEMENT)
    answer = progression_list[answer_index]
    question = get_string_of_progression(
        progression=progression_list, index=answer_index
    )
    return question, answer
