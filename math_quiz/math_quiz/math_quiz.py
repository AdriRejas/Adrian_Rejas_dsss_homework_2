import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.
    :param min_value: The minimum value for the random integer.
    :param max_value: The maximum value for the random integer.
    :return: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Randomly choose an operator from '+', '-', and '*'.
    :return: A random operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_answer(n1, n2, operator):
    """
    Calculate the result of a math operation based on two numbers and an operator.
    :param n1: The first number.
    :param n2: The second number.
    :param operator: The math operator.
    :return: A tuple containing the question string and the calculated answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': 
        answer = n1 + n2
    elif operator == '-': 
        answer = n1 - n2
    else: 
        answer = n1 * n2
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 3  # You can adjust this value to the number of questions you'd like to ask

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = generate_random_integer(1, 10)  
        n2 = generate_random_integer(1, 5)  
        operator = choose_operator()

        problem, correct_answer = calculate_answer(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
