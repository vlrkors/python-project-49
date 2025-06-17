from brain_games.games.engine import generate_progression, run_game


def main():

    name_game = "brain-progression"
    run_game(name_game, generate_progression)


if __name__ == "__main__":

    main()