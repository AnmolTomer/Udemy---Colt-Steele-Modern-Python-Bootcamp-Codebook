# 89. exercise_steps.py
#  Print the stairs using for and while loops.
#  Noob way to do so is that by multiplying the string by a number to print it multiple times.
#  Better approach would be to use the nested loops one loop to change the row number and another loop to print the number of times the smiley face gets printed .

# While loop implementation
# i = 1
n = int(input("Enter the number of rows you want to print in the stair "))
# while i in range(1,n):
#     print("\U0001f600 "*i)
#     # print("\n") Not required
#     i += 1


# For loop implementation
# for num in range(1,n+1): # n+1 to avoid the condition where user enters 5 rows to be printed and there are 4 shown because range works till n-1 elements.
    # print("\U0001f600 "*num)


# Another way to print multiple emoji is :
# t = int(input("Enter the number of times you want to print the entire pattern of steps, {n}"))
# for x in range(t): # Number of times to print the entire step
#     for num in range(0,n+1):
#         print("\U0001f600 "*num)

#  Without string multiplication - UGLIEST SOLUTION
# for x in range(1,n+1):
#     count = 1
#     smileys = ""
#     while count <=  x:
#         smileys += "\U0001f600 "
#         count += 1
#     print(smileys)

