# 88. while_loops_password.py

#  Use Case 1 : To check if a given password is correct or not

# msg = input("What is the password ? ")
# while msg != "minion_bannanaa":
#     print("Uhh Oh...! Wrong Password.")
#     msg = input("What is the password ? ")
#     continue
# print("~~~~~~~YeeeHaw...! ^_^ Correct Password. Welcome to the club minion. :D ~~~~~~~~~~~~~~~~~")


#  Use Case 2

#  To print numbers :
    # Way to do it in for
# for num in range (1,11):
#     print(num)

#  Using while loop :
num = 1 # Initialising the var.
while num < 11 : # or just use while num <= 10
    print(num) # Can't just leave the loop here else it will go to an infinite loop as the value of num remains one always. So we will have to increment the value of num.
    num += 1 # similar to saying num = num + 1
#  Here the idea is same as for loop but we have to declare the variable first and then update it manually each time till the condition is satisfied.
# To print the odd numbers just increment the value by 2 instead of 1.
#  While is more flexible and is a single statement that continues to run until the condition is false. Just take care of infinite loops you shall be worthy to possess the power
#  of while loops.
#  Both loops we can loop a specific number of times but on top of that the while loop is more flexible in the sense that it might run once or 1000 times depending on the
#  input received or data received from a database and is built upon a boolean expression.
#  If we need something to happen a certain number of times and we already know how many times we want it to happen then we can use for loop as it is easy to understand and very
#  simple to implement in the code and you do not have to worry about infinite loop or a boolean condition according to your requirements.
