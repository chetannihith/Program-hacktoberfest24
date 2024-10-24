def text_adventure():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. There are two paths in front of you.")
    
    choice1 = input("Do you want to go left or right? (l/r): ").lower()
    
    if choice1 == 'l':
        print("You encounter a wild animal!")
        choice2 = input("Do you want to run or fight? (run/fight): ").lower()
        if choice2 == 'run':
            print("You safely escaped the forest. You win!")
        else:
            print("You bravely fight the animal but unfortunately lose. Game Over.")
    elif choice1 == 'r':
        print("You find a treasure chest!")
        choice2 = input("Do you want to open it or leave it? (open/leave): ").lower()
        if choice2 == 'open':
            print("Congratulations! You found a pile of gold. You win!")
        else:
            print("You leave the treasure and exit the forest safely. Game Over.")
    else:
        print("Invalid choice. Please restart the game.")

if __name__ == "__main__":
    text_adventure()
