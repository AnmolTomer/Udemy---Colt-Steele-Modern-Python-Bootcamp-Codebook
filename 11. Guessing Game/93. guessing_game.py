# Make 2 programs which will do the following
#  1. Simple guessing game and computer picks a random number and you have to guess it and you get hints if you are too high or too low until you finally get it.
#  2. Rock Paper Scissors with ability to set the loop to check best of x number of games and have a global value.
from random import randint
a = randint(1,10) # Generating random numbers between 1 to 10.
num = None #Number that user gives and is compared with the randint.
# Method 1. Doesn't allows user to play again without restarting.
'''
while a != num :
    num = int(input("Enter the number between 1 to 10 : "))
    if(a == num):
        print(f"You said {num} as the number and computer selected number was indeed {a} .")
    elif a > num :
        print("Too low !")
    else:
        print("Too high !")
   
    b = input("Do you want to keep playing ? y/n")
    if b == 'y':
        num = int(input("Enter the number between 1 to 10 : "))
    elif b == 'n':
        print("Thanks for playing.")
 '''

# Method 2 Loops forever until user enters the break out of loop condition.
while True:
    num = int(input("Enter the number between 1 to 10 : "))
    if a < num:
        print("Too high.")
    elif a > num :
        print("Too low !")
    else:
        print(f"You said {num} as the number and computer selected number was indeed {a} .")
        play_again = input("Do you want to play again ? (y/n) ")
        if play_again == 'y' :
            a = randint(1,10)
            num = None
        else:
            print("Thank you for playing!")
            break