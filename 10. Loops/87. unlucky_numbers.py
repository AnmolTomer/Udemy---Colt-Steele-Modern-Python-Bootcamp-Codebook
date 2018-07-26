# Exercise : Print numbers from 1 to 20 and then do the following
#  For 4 and 13 , print "x is unlucky"....for even numbers print "x is even", for odd numbers, print "x is odd."
for x in range(1,21): # Using 21 since range is exclusive for last element and to make it print from 1 to n we have to start from 1 to n-1.
    if (x % 2 != 0 and x != 4 and x != 13):  # Using modulo to check if remainder is there or not after division by 2 of the specific number.
        print(x, " is odd.")
    elif (x % 2 == 0 and x != 4 and x != 13):
        print(x, " is even.")
    else:
        print(x, " is UNLUCKY !")