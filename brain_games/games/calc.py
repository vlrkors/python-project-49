from games.engine import generate_expression


def get_question_and_answer():
    
    """Генерируем вопрос 
    и правильный ответ для игры calc."""
    expression, correct_answer = generate_expression()
    return expression, str(correct_answer)
