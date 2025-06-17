from brain_games.games.engine import run_game
from brain_games.games.gcd import generate_question_and_answer


def main():

    name_game = "brain-gcd"
    welcome_question = "Find the greatest common divisor of given numbers."
    run_game(name_game, welcome_question, generate_question_and_answer)


if __name__ == "__main__":

    main()
