#The less basic version for rock paper scissors.
#  Featuring the dumbest AI ever as computer player.

print("                            ...Rock...                                                             ")
print("                            ...Paper...                                                             ")
print("                            ...Scissors...                                                             \n \n")

import random
# Computer opponent picks random thing.
# random.randint(0,2)
# We are including the module called random it is like the code that is already built in python but it is not fully built in the sense that you have to import it.
# from module_name import module_specific_function
# module_name.module_function(parameters )
# Touch rps_5.py
# random.randint(a,b) Returns a random integer N such that a <= N <= b that is including the extreme values as well.
#Now we use this to write a conditional set of instructions that says that if the random is zero or one or two then computer is equal to rock paper or scissors keeping the subsets of player1 and player 2 same 
# Only difference being is that now we have computer and only one player.
# Making a variable to store the value received from the random integer module.
# player = input("Player, make your move: ").lower()
# rand_num = randint(0,2)
# # We can do from 1 to 3 or -5 to -7 or any 3 numbers that we want but we are doing this zero indexed as things are in computer generally.

# if rand_num == 0:
#     computer = "rock"
# elif rand_num == 1:
#     computer = "paper"
# elif rand_num == 2:
#     computer = "scissors"
# print(computer)
#print(f"Computer plays {computer}" )
# if player == computer:
#     print("It is a tie.")

# elif player == "rock":
# 	if computer == "scissors":
# 		print("player wins.")
# 	elif computer == "paper":
# 		print("computer wins.")

# elif player == "paper":
# 	if computer == "rock":
# 		print("player wins.")
# 	elif computer == "scissors":
# 		print("computer wins.")

# elif player == "scissors":
# 	if computer == "paper":
# 		print("player wins.")
# 	elif computer == "rock":
# 		print("Computer wins.")
# else:   
# 	print("Something went wrong.")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays" + computers )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")
