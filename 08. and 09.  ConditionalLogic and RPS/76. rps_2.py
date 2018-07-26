# We had human players in the first version of the game.
# Now in this version we are going to go up in this one when it comes to code method and as well as not making the code too lengthy.
print("Rock")
print("Paper ")
print("Scissors ...")

player1 = input("Player 1 make your move: ")
player2 = input("Player 2 make your move: ")

if player1 == "rock" and player2 == "scissors":
	print("player1 wins.")
elif player1 == "rock" and player2 == "paper":
	print("player2 wins.")
elif player1 == "paper" and player2 == "rock":
	print("player1 wins.")
elif player1 == "paper" and player2 == "scissors":
	print("player2 wins.")
elif player1 == "scissors" and player2 == "paper":
	print("player1 wins.")
elif player1 == "scissors" and player2 == "rock":
	print("player2 wins.")
elif player1 == player2:
	print("It is a tie boii.")
else:
	print("Something went wrong. Try entering your input in all small letters. e.g. rock, paper, scissors.")

### Gives the error of player 1 wins as a result most of the times excluding the few cases where player 2 wins sometimes.
# if player1 == "rock" or "Rock" and player2 == "scissors" or "Scissors":
# 	print("Player 1 Wins...!")
# elif player1 == "rock" or "Rock" and player2 == "paper" or "Paper":
# 	print("Player 2 wins.")
# elif player1 == "paper" or "Paper" and player2 == "scissors" or "Scissors":
# 	print("Player 2 wins.")
# elif player1 == "paper" or "Paper" and player2 == "rock" or "Rock":
# 	print("Player 1 wins... 1")
# elif player1 == "scissors" or "Scissors" and player2 == "paper" or "Paper":
# 	print("Player 1 wins...!")
# elif player1 == "scissors" or "Scissors" and player2 == "rock" or "Rock":
# 	print("Player 2 wins...!")

### The long way of implementing how to declare that it is a tie.
# elif player1 == "rock" or "Rock" and player2 == "rock" or "Rock":
# 	print("It's a draw boii....!!")
# elif player1 == "paper" or "Paper" and player2 == "paper" or "Paper":
# 	print("It's a draw boii....!!")
# elif player1 == "scissors" or "Scissors" and player2 == "scissors" or "Scissors":
# 	print("It's a draw boii....!!")	

## Another way to show ties is that we use if player1 == player2 then it is draw too.
# elif player1 == player2:
# 	print("It's a tie boii!")
# else:
# 	print("U wot m8!")