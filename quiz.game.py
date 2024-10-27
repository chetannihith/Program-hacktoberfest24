def quiz_game():
    questions = {
        "What is the capital of France?": ["a) Paris", "b) London", "c) Rome", "d) Berlin"],
        "What is 2 + 2?": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "What is the color of the sky?": ["a) Green", "b) Blue", "c) Red", "d) Yellow"]
    }
    
    score = 0
    
    print("Welcome to the Simple Quiz Game!")
    
    for question, options in questions.items():
        print(question)
        for option in options:
            print(option)
        
        answer = input("Your answer (a/b/c/d): ").lower()
        
        if (question == "What is the capital of France?" and answer == 'a') or \
           (question == "What is 2 + 2?" and answer == 'b') or \
           (question == "What is the color of the sky?" and answer == 'b'):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
