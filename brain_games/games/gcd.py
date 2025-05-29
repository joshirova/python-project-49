import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer