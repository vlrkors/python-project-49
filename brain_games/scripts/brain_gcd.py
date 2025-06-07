from games.engine import run_game
from games.gcd import get_question_and_answer


def start_game():
    """
    Запускает игру "Наибольший общий делитель (НОД)".
    """
    print("Find the greatest common divisor of given numbers.")
    run_game(get_question_and_answer)

if __name__ == "__main__":
    start_game()