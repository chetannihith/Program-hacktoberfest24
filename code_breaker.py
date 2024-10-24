import random

def generate_code(length=4):
    """Generates a random code of unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:length]

def get_clues(guess, secret_code):
    """Provides clues based on the player's guess."""
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            clues.append("Correct")
        elif guess[i] in secret_code:
            clues.append("Close")
    if not clues:
        return ["Nope"]
    return clues

def play_game():
    print("Welcome to 'Code Breaker'!")
    print("I have generated a secret 4-digit code with unique numbers.")
    print("Your goal is to guess the code.")
    print("Feedback: 'Correct' means right digit in the right place, 'Close' means right digit but wrong place, 'Nope' means no correct digits.")
    
    secret_code = generate_code()
    attempts = 0
    
    while True:
        guess = input("Enter your 4-digit guess (unique digits only): ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter 4 unique digits.")
            continue
        
        guess = [int(digit) for digit in guess]
        attempts += 1
        
        if guess == secret_code:
            print(f"Congratulations! You cracked the code {secret_code} in {attempts} attempts.")
            break
        else:
            clues = get_clues(guess, secret_code)
            print("Clues: ", " ".join(clues))

if __name__ == "__main__":
    play_game()
