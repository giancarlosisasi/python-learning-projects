import random
from dice import DICE, DICE_HEIGHT, DICE_FACE_SEPARATOR


def play():
    number_dice = 0
    user_input = input("""
Welcome to dice-roller game!
How many dice do you want to roll? [1-6] """)

    try:
        number_dice = int(user_input)
    except ValueError:
        print("Not a valid number")
        return

    # create a list with the faces of dices that we need to print
    dice_faces = []
    for _ in range(number_dice):
        face_idx = random.randrange(0, 6) + 1
        dice_faces.append(DICE[face_idx])

    """Print an ASCII diagram of dice faces from `dice_values`.

    The string printed contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    printed looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    dice_faces_rows = []
    for row_idex in range(DICE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idex])

        row_string = DICE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    header = "  RESULTS  ".center(width, "~")
    print("\n".join([header] + dice_faces_rows))


if __name__ == "__main__":
    play()
    while input("Do you want to play again? (Y/N) ") == "Y":
        play()
