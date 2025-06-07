from brain_games.games.engine import run_game
from brain_games.games.gcd import generate_question_and_answer


def main():
    """
    Запускаем игру "Наибольший общий делитель (НОД)".
    """
    print("Find the greatest common divisor of given numbers.")
    run_game(generate_question_and_answer)


if __name__ == "__main__":

    main()
