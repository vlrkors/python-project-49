from brain_games.games.engine import generate_progression, run_game


def main():

    # Используем функцию generate_progression для генерации вопросов и ответов
    name = run_game(generate_progression)
    if name:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":

    main()