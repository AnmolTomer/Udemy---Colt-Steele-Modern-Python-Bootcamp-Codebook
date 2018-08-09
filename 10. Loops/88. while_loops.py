# Both while and for can be used to iterate over a collection what you can do with for loop you can also do with the for loop.
# But the catch is that there are lots of things that you can do with a while loop which you cannot do with the for loop.
#  Structure of while loop is something like this :
# while (boolean_expression):
    # seek caffeine
# While loop is trye then condition keeps running and at the point that condition becomes false then the loop stops.
user_response = input("Enter something : ")
while user_response != "please":
    user_response = input("Ah ah ah, you didn't say the magic word: ")
    if user_response == "please":
        name = input("Enter your name user : ")
        age = int(input("Enter your age :"))
        reg_no = str(input("Enter your registeration number : "))
        print(f"Your details are {name} is name, {age} is age and {reg_no} is registeration number")
#  While loops require more careful setup than for loops, since you have to specify the termination conditions manually.
#  Be careful that if the condition does not becomes false at some point, your loop will continue forever.
