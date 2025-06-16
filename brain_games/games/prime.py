import random
from brain_games.games.engine import is_prime


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ."""
    number = random.randint(1, 100)  # Генерируем случайное число от 1 до 100
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
