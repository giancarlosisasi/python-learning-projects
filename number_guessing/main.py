import random


def play():
    GAME_STATE = "playing"
    guess_number = random.randint(1, 10)

    print("Welcome to guess number!\n(write exit to close the game)")
    while GAME_STATE == "playing":
        user_guess = input("What number I'm thinking? ")

        if user_guess == "exit":
            GAME_STATE = "exit"
            continue

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess == guess_number:
            print("Congrats! You win")
            GAME_STATE = "exit"
        else:
            print("Ups! That's not correct. Try again")


if __name__ == "__main__":
    play()
