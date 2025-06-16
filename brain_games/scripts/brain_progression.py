from brain_games.games.engine import run_game, generate_progression


def main():
    # Используем функцию generate_progression для генерации вопросов и ответов
    name = run_game(generate_progression)
    if name:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":

    main()