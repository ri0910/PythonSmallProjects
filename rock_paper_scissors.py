import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper and 's' for scissors \n").lower()
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'Tie'
    elif is_win(user,computer):
        return 'You won !'
    else:
        return 'You lost !'
    
def is_win(user,computer):
    if ( user == 'r' and computer == 's') or ( user == 'p' and computer == 'r') or ( user == 's' and computer == 'p'):
        return True


print(play())