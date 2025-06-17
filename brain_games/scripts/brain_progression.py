from brain_games.games.engine import generate_progression, run_game


def main():

    name_game = "brain-progression"
    welcome_question = "What number is missing in the progression?"
    run_game(name_game, welcome_question, generate_progression)


if __name__ == "__main__":

    main()