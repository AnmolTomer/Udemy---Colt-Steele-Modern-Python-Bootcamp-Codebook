# Will do refactoring to make the code look good instead of the previous version.

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1 Enter your choice: ")
player2 = input("Player 2 Enter your choice: ")

#Refactoring by writing and statement with 2 nested conditionals for making the code smaller significantly.

# Placing the condition of draw on the top since there are multiple ways of achieving a draw and others are elif and they will only run if the main tie condition fails so not letting the computer to
# check for the rock paper scissors cases when the input is same leading to more efficient code.

if player1 == player2:
	print("It is a tie.")

elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins.")
	elif player2 == "paper":
		print("player2 wins.")

elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins.")
	elif player2 == "scissors":
		print("player2 wins.")

elif player1 == "scissors":
	if player2 == "paper":
		print("player1 wins.")
	elif player2 == "rock":
		print("player2 wins.")

# The ones which follow an if need to be made into elif because only one of them will have to be true.
else:
	print("Something went wrong.")



# Here's another potential solution that is much shorter.  Rather than individually checking for the conditions that lead to a player2 win,
# they're all lumped together using the else :



# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")

# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")
# The only issue with this version is that it will print "p2 wins" if either user enters an invalid move like "pizza".
# It doesn't have the error-checking of the previous solution detailed in the video.  But as far as the pure RPS logic, this is a clean approach.