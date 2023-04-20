import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number : "))
        if guess > random_number:
            print("Number is too large")
        elif guess < random_number:
            print("Number is too small")
    print(f"Congratulations, You have guessed number {random_number} correctly !")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if high != low:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"if {guess} is the correct number then press 'C' , if it is high then press "
        + "H or if it is low then press L : ").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f"Yayy ! Computer guessed the correct number {guess}")

computer_guess(10)