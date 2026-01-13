import random

MAX_ATTEMPTS = 7
score = 0


def choose_difficulty():
    #Select difficulty level
    print("\nChoose Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter choice: ")

    if choice == "1":
        return 10
    elif choice == "2":
        return 50
    elif choice == "3":
        return 100
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10


def get_user_guess(limit):
    #Take user guess with validation
    try:
        guess = int(input(f"Guess a number (1–{limit}): "))
        if 1 <= guess <= limit:
            return guess
        else:
            print("Number out of range.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def give_hint(guess, secret):
    """AI-like hint system"""
    if guess < secret:
        print("📉 Too low!")
    elif guess > secret:
        print("📈 Too high!")


def play_game():
    #Main game logic
    global score

    limit = choose_difficulty()
    secret_number = random.randint(1, limit)
    attempts = 0

    print("\nGame Started!")

    while attempts < MAX_ATTEMPTS:
        guess = get_user_guess(limit)
        if guess is None:
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed in {attempts} attempts.")
            score += 1
            break
        else:
            give_hint(guess, secret_number)
            print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

    else:
        print(f"Game Over! The number was {secret_number}")

    print(f"Score: {score}")


def main():
    #Game loop
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
