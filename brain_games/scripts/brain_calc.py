import random

from games.calc import GAME_NAME, get_question_and_answer
from games.engine import run_game


def generate_expression():

    """
    Генерируем случайное математическое выражение c операциями +, -, *.
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num1 = random.randint(1, 20)  # Случайное число от 1 до 20
    num2 = random.randint(1, 20)  # Случайное число от 1 до 20
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    
    expression = f"{num1} {operator} {num2}"
    return expression, result


def main():

    run_game(get_question_and_answer)


if __name__ == "__main__":

    main()
