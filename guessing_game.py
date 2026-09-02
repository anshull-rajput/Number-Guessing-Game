import random


def play_game():
    levels = {
        "1": ("Easy", 1, 50, 10),
        "2": ("Medium", 1, 100, 7),
        "3": ("Hard", 1, 200, 5),
    }

    print("\n🎯 Number Guessing Game")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    while True:
        choice = input("Choose a level (1/2/3): ").strip()
        if choice in levels:
            break
        print("Please choose 1, 2, or 3.")

    level, low, high, max_attempts = levels[choice]
    number = random.randint(low, high)

    print(f"\n{level} level: Guess a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{max_attempts}: "))
                if low <= guess <= high:
                    break
                print(f"Enter a number between {low} and {high}.")
            except ValueError:
                print("Please enter a valid number.")

        if guess == number:
            print(f"\n✅ Correct! You won in {attempt} attempt(s).")
            return
        if guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"\n❌ Game over! The number was {number}.")


while True:
    play_game()
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
