import random


def generate_expression():

    """
    Генерируем случайное математическое выражение c операциями +, -, *.
    """
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    
    expression = f"{num1} {operator} {num2}"
    return expression, result


def run_game(get_question_and_answer, max_rounds=3):

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(max_rounds):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
                  Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")