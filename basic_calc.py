def add(a,b):
    ans = a + b
    print(str(a) + " + " + str(b) + " = " + str(ans))

def sub(a,b):
    ans = a - b
    print(str(a) + " - " + str(b) + " = " + str(ans))

def mul(a,b):
    ans = a * b
    print(str(a) + " * " + str(b) + " = " + str(ans))

def div(a,b):
    ans = a / b
    print(str(a) + " / " + str(b) + " = " + str(ans))

while True:
    print(" Enter 'A' for addition \n Enter 'S' for subtraction \n Enter 'M' for multiplication \n Enter 'D' for division \n")
    choice =  input("Enter you choice : ").lower()
    if choice == 'a':
        print("* Addition *")
        a =int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        add(a,b)
    elif choice == 's':
        print("* Subtraction *")
        a =int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        sub(a,b)
    elif choice == 'm':
        print("* Multiplication *")
        a =int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        mul(a,b)
    elif choice == 'd':
        print("* Division *")
        a =int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        div(a,b)
    else:
        exit()