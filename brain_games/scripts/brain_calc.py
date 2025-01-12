import random

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(["+", "-", "*"])
    
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    elif operator == "*":
        correct_answer = num1 * num2
    
    question = f"{num1} {operator} {num2}"
    return question, str(correct_answer)

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    
    for _ in range(3):
        question, correct_answer = generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
