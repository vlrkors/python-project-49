import random

from ..games.calc import get_question_and_answer
from ..games.engine import run_game


def generate_expression():

    """
    Генерируем случайное математическое выражение c операциями +, -, *.
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num1 = random.randint(1, 20)  # NOSONAR
    num2 = random.randint(1, 20)  # NOSONAR
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    
    expression = f"{num1} {operator} {num2}"
    return expression, result


def main():

    name_game = "brain-calc"
    welcome_question = "What is the result of the expression?"
    run_game(name_game, welcome_question, get_question_and_answer)


if __name__ == "__main__":

    main()
