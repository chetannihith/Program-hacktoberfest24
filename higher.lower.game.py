import random

def higher_lower_game():
    print("Welcome to the Higher or Lower Game!")
    
    score = 0
    current_number = random.randint(1, 100)
    
    while True:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be higher or lower? (h/l): ").lower()
        
        next_number = random.randint(1, 100)
        print(f"The next number is: {next_number}")
        
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            print("Correct! You get a point.")
            score += 1
            current_number = next_number
        else:
            print(f"Wrong! Your score is: {score}")
            break
    
    print("Game Over!")

if __name__ == "__main__":
    higher_lower_game()
