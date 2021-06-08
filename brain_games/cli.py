import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    username = prompt.string(prompt="May I have your name? ")
    print("Hello, %s!" % username)
