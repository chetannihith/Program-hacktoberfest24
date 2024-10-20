
import random

# List of trivia questions and answers
questions = [
    ("What is the capital of France?", "Paris"),
    ("How many continents are there?", "7"),
    ("Who wrote 'Harry Potter'?", "J.K. Rowling"),
    ("What is the tallest mountain in the world?", "Mount Everest"),
    ("What is the chemical symbol for water?", "H2O"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who was the first president of the United States?", "George Washington"),
    ("What is the largest mammal?", "Blue Whale"),
    ("Which ocean is the largest?", "Pacific Ocean"),
    ("What year did the Titanic sink?", "1912")
]

def ask_question(question, answer):
    user_answer = input(f"{question}\nYour answer: ")
    return user_answer.strip().lower() == answer.lower()

def start_quiz():
    print("Welcome to the Fun Trivia Quiz!")
    print("Let's see how much you know!")
    
    random.shuffle(questions)  # Shuffle the questions to make it random
    score = 0
    
    for i in range(5):  # Ask 5 random questions
        question, answer = questions[i]
        if ask_question(question, answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Oops! The correct answer was: {answer}\n")
    
    # Final score and playful response
    print(f"Your final score is: {score}/5")
    if score == 5:
        print("You're a trivia master! Amazing!")
    elif score >= 3:
        print("Great job! You know quite a lot!")
    else:
        print("Keep trying! You'll get better with practice!")

if __name__ == "__main__":
    start_quiz()
