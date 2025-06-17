import random

import prompt


def get_random_number():

    """Генерация случайного числа"""
    return random.randint(1, 100)


def main(): 

    """Предлагает пользователю проверить на четность случайно \
    сгенерированные число."""
    # Вывод приветствия и запрос имени пользователя
    print("brain-even\n")
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Описание правил игры
    print('Answer "yes" if the number is even, ',
          'otherwise answer "no".')

    # Количество вопросов для победы
    correct_answers = 0
    total_questions = 3

    while correct_answers < total_questions:
        # Генерация случайного числа
        number = get_random_number()
        print(f"Question: {number}")

        # Получение ответа от пользователя
        user_answer = input("Your answer: ").lower()

        # Проверка корректности ввода
        if user_answer not in ["yes", "no"]:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was 'yes' or 'no'.")

            print(f"Let's try again, {name}!")
            return

        # Проверка четности числа
        is_even = True if number % 2 == 0 else False
        correct_response = "yes" if is_even else "no"

        # Сравнение ответа пользователя с правильным ответом
        if user_answer == correct_response:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_response}'.")

            print(f"Let's try again, {name}!")
            return

    # Поздравление после успешной игры
    print(f"Congratulations, {name}!")


# Запуск игры
if __name__ == "__main__":

    main()