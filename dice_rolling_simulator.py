import random

def dice_rolling():
    dices = {
        1: (
        "------",
        "|     |",
        "|     |",
        "| O   |",
        "|     |",
        "|     |",
        "------"
        ),
        2: (
        "------",
        "|     |",
        "|     |",
        "| O   |",
        "|   O |",
        "|     |",
        "------"
        ),
        3: (
        "------",
        "|     |",
        "|   O |",
        "| O   |",
        "|   O |",
        "|     |",
        "------"
        ),
        4: (
        "------",
        "| O   |",
        "|   O |",
        "| O   |",
        "|   O |",
        "|     |",
        "------"
        ),
        5: (
        "------",
        "|    O|",
        "| O   |",
        "|   O |",
        "| O   |",
        "|   O |",
        "------"
        ),
        6: (
        "------",
        "|     |",
        "| O O |",
        "| O O |",
        "| O O |",
        "|     |",
        "------"
        )
    }

    roll = input("Roll the dice ? (yes/no): ").lower()
    while roll == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Rolled dices are {dice1} and {dice2}.")
        print("\n".join(dices[dice1]))
        print("\n".join(dices[dice2]))
        roll = input("Roll again ? : ")

dice_rolling()