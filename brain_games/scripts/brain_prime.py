from brain_games.games.engine import run_game
from brain_games.games.prime import generate_question_and_answer


def main():

    name_game = "brain-prime"
    welcome_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(name_game, welcome_question, generate_question_and_answer)


if __name__ == "__main__":
    main()