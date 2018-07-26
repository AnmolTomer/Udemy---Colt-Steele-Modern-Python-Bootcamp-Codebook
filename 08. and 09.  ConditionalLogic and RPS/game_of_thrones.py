print("Heyy there! Welcome to GOT quotes machine.")
print("What is your name human ?")
user_name = input()
print("\n Select from numbers 1 through 5 and we will give a quote (or two) based on your name. e.g. 1 or Tyrion or TL (case sensitive)\n \n")
# or First Name or Initials
print("What's your character's name?\n 1. Tyrion Lannister \n 2. Cersei Lannister \n 3. Daenerys Targaryen \n 4. Ned Stark \n 5. Ygritte \n ")
name = input("Enter your input here: ")

if name == "1": # or "Tyrion" or "TL":
    print("Here are some of the Tyrion Lannister quotes:\n 1. The powerful have always preyed on the powerless. That's how they became powerful in the first place.")
    print("2. Let me give you some advice, bastard. Never forget what you are. The rest of the world will not. Wear it like armor, and it can never be used to hurt you.")
    print("3. A lion doesn't concern himself with the opinions of a sheep.")
    print("4. It's easy to confuse 'what is' with 'what ought to be', especially when 'what is' has worked out in your favor.")
elif name == "2": # or "Cersei" or "CL":
    print("1. If you ever call me 'sister' again, I'll have you strangled in your sleep.")
    print("2. When you play the game of thrones, you win or you die.")
elif name == "3": # or "Daenerys" or "DT":
    print("1. The next time you raise a hand to me will be the last time you have hands.")
elif name == "4": # or "Ned" or "NS":
    print("Winter is coming.")
elif name == "5": # or "Ygritte" or "Y":
    print("You know Nothing! Jon Snow!")
else:
    print("Please read the first line where at the end we give examples about how to enter name to get character quotes.\nProgram will exit now. Re-run if you actually need GOT quotes and are not here for QA testing of my code.")
    print(f"You just need to read and feed in right input {user_name}. C'mon {user_name} you can do it! :) ")
# Suggestion for future based on key words in quotes make an alexa function that recognizes who said it .