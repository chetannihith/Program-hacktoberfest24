import json
from datetime import datetime

# Define the filename to store the exercise log
FILENAME = 'exercise_log.json'


def load_exercises():
    """Load exercises from the JSON file."""
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_exercises(exercises):
    """Save exercises to the JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(exercises, file)


def log_exercise():
    """Log a new exercise."""
    exercises = load_exercises()

    exercise_type = input("Enter the type of exercise (e.g., Running, Cycling): ")
    duration = float(input("Enter the duration in minutes: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    exercise = {
        'type': exercise_type,
        'duration': duration,
        'date': date
    }
    exercises.append(exercise)
    save_exercises(exercises)

    print(f"Logged {exercise_type} for {duration} minutes on {date}.")


def view_exercises():
    """View all logged exercises."""
    exercises = load_exercises()

    if not exercises:
        print("No exercises logged yet.")
        return

    print("\nLogged Exercises:")
    for i, exercise in enumerate(exercises, 1):
        print(f"{i}. {exercise['type']} - {exercise['duration']} minutes on {exercise['date']}")
    print()


def calculate_total_duration():
    """Calculate the total duration of all exercises."""
    exercises = load_exercises()
    total_duration = sum(exercise['duration'] for exercise in exercises)
    print(f"Total duration of exercises: {total_duration} minutes\n")


def main():
    """Main function to run the fitness tracker app."""
    while True:
        print("Fitness Tracker App")
        print("1. Log Exercise")
        print("2. View Exercises")
        print("3. Total Duration")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            log_exercise()
        elif choice == '2':
            view_exercises()
        elif choice == '3':
            calculate_total_duration()
        elif choice == '4':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
