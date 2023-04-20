print("******** WELCOME TO MY FIRST GAME ***********")

name = input("What is your name ? ")
print("Hello ", name)
age = int(input("What is your age ?"))

health = 10

if age >=18:
    print("You are old nough to play")
    wants_to_play = input("Do you want to play ? ").lower()
    if wants_to_play == "yes":
        print("You are starting with {}".format(health))
        print("Let's play :D !!!!")
        left_or_right = input("First choice : Left or Right (left/right) ? ").lower()
        if left_or_right == "left":
            print("Nice , You are following the right path to reach the lake :D")
            ans = input("Do you want to go around or swim across the lake ? (around/across)").lower()
            if ans == "around":
                print("You have reched the other side of the lake")
            elif ans == "across":
                print("You have managed to cross the lake but you were bit by a fish and lost 5 health points.")
                health -= 5
            ans = input("You notice a river and a house. where do you want to go ?(river/house)").lower()
            if ans == "house":
                print("You go to the house and greated the owner... He doesn't like you and you lost 5 health.")
                health -= 5
                if health<=0:
                    print("You lost the game")
                else:
                    print("*****You survived and win the game :D ****")
            else:
                print("You fell in the river and lost !")
        else:
            print("You fall and lost ! :(")
    else:
        print("Cya.....")
else:
    print("Your are not allowed to play")
