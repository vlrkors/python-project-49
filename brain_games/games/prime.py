import random


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ."""
    number = random.randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
