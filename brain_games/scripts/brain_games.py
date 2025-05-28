import prompt

from brain_games.services.services import get_random_number

from ..brain_games import cli


def main():
    
    cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    number_question = get_random_number()
    print(f'Question: {number_question}')
    answer = prompt.string('Your answer: ')
    print(f'answer: {answer}')


if __name__ == "__main__":
    
    main()