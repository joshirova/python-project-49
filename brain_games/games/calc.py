import random

RULE = 'What is the result of the expression?'

def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    question = f"{num1} {operator} {num2}"
    return question, str(correct_answer)