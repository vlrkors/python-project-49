from brain_games.games.engine import generate_progression, run_game


def main():

    # Используем функцию generate_progression для генерации вопросов и ответов
    run_game(generate_progression)


if __name__ == "__main__":

    main()