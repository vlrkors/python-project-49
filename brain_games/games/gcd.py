import random
from math import gcd


def generate_question_and_answer():
    
    """
    Генерирует два случайных числа 
    и вычисляет их наибольший общий делитель (НОД).
    Возвращает строку c вопросом и правильный ответ.
    """
    num1 = random.randint(1, 100)  # NOSONAR
    num2 = random.randint(1, 100)  # NOSONAR
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))  # Находим НОД с помощью функции gcd
    return question, correct_answer