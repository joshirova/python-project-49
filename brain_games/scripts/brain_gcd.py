import random
import math

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        correct_answer = math.gcd(number1, number2)

        print(f"Question: {number1} {number2}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

