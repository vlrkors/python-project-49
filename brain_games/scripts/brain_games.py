import prompt

from brain_games.scripts.services import get_random_number


def main():
    print("Welcome to brain-games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no"')
    number_question = get_random_number
    print(f'Question: {number_question}')


if __name__ == "__main__":
    main()
