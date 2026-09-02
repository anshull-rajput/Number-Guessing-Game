import random

number = random.randint(1, 100)
attempts = 0

print("\nNumber Guessing Game")
print("Guess a number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not 1 <= guess <= 100:
        print("Please choose a number from 1 to 100.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
