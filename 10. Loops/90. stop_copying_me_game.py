# Exercise question to take an input and keep printing it back again as long as the user enters a specific phrase and to exit upon receiving that phrase.
a = input("Enter what you want to say : ")

#Method - 1
while a != "stop copying me" :
    a = input(f"{a}\n")
print("UGH FINE YOU WIN, BROTHER")
# Method - 2
# while a != "stop copying me" :
#     print(a)
#     a = input()
# print("UGH FINE YOU WIN, BROTHER")