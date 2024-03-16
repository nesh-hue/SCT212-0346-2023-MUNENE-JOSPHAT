import random


def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])

    if operator == '+':
        answer = num1 + num2
        question = f"{num1} + {num2}"
    else:
        answer = num1 - num2
        question = f"{num1} - {num2}"

    return question, answer


def main():
    print("Welcome to the Simple Math Quiz!")
    print("Answer 'q' to quit.")

    while True:
        question, correct_answer = generate_question()
        user_input = input(f"What is {question}? ")

        if user_input.lower() == 'q':
            break

        try:
            user_answer = int(user_input)

            if user_answer == correct_answer:
                print("Correct!")
            else:
                print("Incorrect!")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
