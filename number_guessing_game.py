import random

print("=" * 35)
print("NUMBER GUESSING GAME".center(35))
print("=" * 35)

while True:

    attempts = 0

    print()
    print("Select Difficulty")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print()

    # Difficulty Selection
    while True:

        choice = int(input("Enter your choice: "))

        if choice == 1:
            number = random.randint(1, 10)
            break

        elif choice == 2:
            number = random.randint(1, 50)
            break

        elif choice == 3:
            number = random.randint(1, 100)
            break

        else:
            print("Invalid Choice! Please try again.")

    # Guessing Game
    while True:

        guess = int(input("Guess The Number: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed correctly.")
            print(f"You guessed the number in {attempts} attempts.")
            break

        elif guess < number:
            print("Too Low! Try Again.")

        else:
            print("Too High! Try Again.")

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        continue
    
    else:
        print("\nThank you for playing!")
        break