from brain_games.games.engine import run_game
from brain_games.games.prime import generate_question_and_answer


def main():
    run_game(generate_question_and_answer)


if __name__ == "__main__":
    main()