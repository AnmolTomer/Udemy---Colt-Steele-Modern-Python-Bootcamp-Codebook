# Exercise : Print numbers from 1 to n given by the user and then do the following
#  For 4 and 13 , print "x is unlucky"....for even numbers print "x is even", for odd numbers, print "x is odd."
n = int(input("Enter the number upto which you want to print and see which numbers in between are even or odd: \n"))
for x in range(1,n+1):
    if (x % 2 != 0 and x != 4 and x != 13):  # Using modulo to check if remainder is there or not after division by 2 of the specific number.
        print(x, " is odd.")
    elif (x % 2 == 0 and x != 4 and x != 13):
        print(x, " is even.")
    else:
        print(x, " is UNLUCKY !")
#  Only difference between v2 and v1 is that here user can give an input and program displays all odd even till that number.