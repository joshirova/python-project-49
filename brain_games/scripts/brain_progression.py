import random

def greet_user():
    """Приветствие и запрос имени пользователя."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def generate_progression():
    """Генерация арифметической прогрессии с пропущенным элементом."""
    length = random.randint(5, 10)  # Длина прогрессии (от 5 до 10 чисел)
    start = random.randint(1, 50)  # Начальное число прогрессии
    step = random.randint(1, 10)   # Шаг прогрессии

    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)  # Скрываем случайный элемент
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer

def play_game():
    """Основная логика игры."""
    name = greet_user()
    print("What number is missing in the progression?")
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        question, correct_answer = generate_progression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

def main():
    play_game()

