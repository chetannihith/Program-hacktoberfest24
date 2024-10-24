import random

def roll_dice():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (1-6): "))
            if num_dice < 1 or num_dice > 6:
                print("Please enter a number between 1 and 6.")
                continue
            
            results = [random.randint(1, 6) for _ in range(num_dice)]
            print(f"You rolled: {results}")
            
            play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    roll_dice()
