import random


def get_random_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max) #returns a random integer between min and max

def get_random_operation():
    """
    Randomly selecting a math operator 
    """
    return random.choice(['+', '-', '*']) #randomly chosen operator


def calculate(num1, num2, operator):
    perform = f"{num1} {operator} {num2}"
    if operator == '+': ans = num1 + num2
    elif operator == '-': ans = num1 - num2
    else: ans = num1 * num2
    return perform, ans

def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = get_random_int(1, 15); num2 = get_random_int(1, 5); operator = get_random_operation()

        PROBLEM, ANSWER = calculate(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! You scored: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()