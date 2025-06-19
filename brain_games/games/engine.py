import random


def generate_progression():

    """
    Генерирует арифметическую прогрессию и скрывает случайный элемент.
    Возвращает кортеж (вопрос, правильный ответ).
    """
    # Генерация параметров прогрессии
    start = random.randint(1, 50)  # NOSONAR
    step = random.randint(1, 10)   # NOSONAR
    length = random.randint(5, 10)  # NOSONAR
    
    # Создание прогрессии
    progression = [start + step * i for i in range(length)]
    
    # Выбор случайного индекса для скрытия
    hidden_index = random.randint(0, length - 1) # NOSONAR
    hidden_value = progression[hidden_index]
    
    # Замена скрытого элемента на '..'
    progression[hidden_index] = '..'
    
    # Формирование вопроса
    question = " ".join(map(str, progression))
    
    return question, hidden_value


def generate_expression():

    """
    Генерируем случайное математическое выражение c операциями +, -, *.
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)# NOSONAR
    num1 = random.randint(1, 50)# NOSONAR
    num2 = random.randint(1, 50)# NOSONAR
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    
    expression = f"{num1} {operator} {num2}"
    return expression, result


def run_game(name, welcome_question, get_question_and_answer, max_rounds=3):

    print(name + "\n")    
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(welcome_question)

    for _ in range(max_rounds):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
    return name