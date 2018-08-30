#   Brak : Is what we write to exit the loop whenever we want.

#  1. Example using while loop
'''
while True:
    command = input("Type 'exit' to exit : ")
    if (command == 'exit'):
        break # Halt the execution of the loop.
'''
#  2. Example using for loop
'''
for x in range(1,101):
    print(x)
    if x == 19 :
        break
'''
#  3. Repetitive Room Problem
times = int(input("How many times do I have to tell you ? "))
for time in range(times):
    print("Clean up your ROOM!")
    if time >= 3 :
        print("Do you even listen anymore ?")
        break