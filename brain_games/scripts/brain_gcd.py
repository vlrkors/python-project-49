from brain_games.games.engine import run_game
from brain_games.games.gcd import generate_question_and_answer


def main():

    name_game = "brain-gcd"
    run_game(name_game, generate_question_and_answer)


if __name__ == "__main__":

    main()
