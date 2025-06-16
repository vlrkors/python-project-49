import random
from brain_games.games.engine import run_game
from brain_games.services.services import is_prime


def generate_question_and_answer():
    """Генерирует вопрос и правильный ответ."""
    number = random.randint(1, 100)  # Генерируем случайное число от 1 до 100
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    
    run_game(generate_question_and_answer)

if __name__ == "__main__":
    main()