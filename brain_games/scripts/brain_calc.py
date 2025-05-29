import random


def generate_expression():

    """
    Генерируем случайное математическое выражение с операциями +, -, *.
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

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    print("What is the result of the expression?")
    
    for _ in range(3):  # Игра состоит из 3 раундов
        expression, correct_answer = generate_expression()
        print(f"Question: {expression}")
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(.\
                   Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.\
                   Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":

    main()