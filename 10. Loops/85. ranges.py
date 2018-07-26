#  Blah Blah Blah
#  Ranges exist on their own but they are hardly used outside the for loops and to know for loops we need ranges.
#  Ranges are just simple ways to represent an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.
#  If we just want to print the numbers what we can do is we can iterate over a range.
#  A range is just a defined slice of number line that we have defined.
#  range(7) Showing the end point and it starts from zero and goes upto the last number but does not include it hence it is exclusive.
#  range(1,8) will start at 1 including 1 and stop at 8 excluding 8. Therefore 1 to 7.
#  range(1 , 10, 2) third number is called the step or interval of how many numbers to skip and here we skip 2 everytime and we start from 1. Odd numbers.
#  range(7,0,-1) what this does is that it allows us to move from 7 to 0 and decerementing the value each time by 1. 7 to 1 printed excluding 0.

# # >>> range(10)
# range(0, 10)
# >>> r = range(0,10)
# >>> list(r)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  List will be covered pretty soon.
# >>> nums = range(1, 10, 2)
# >>> list(nums)
# [1, 3, 5, 7, 9]

for num in range(10,20,2):
    print(num)
#  When we write range what it does is it will generate a sequence of numbers that we can use with the for loops.
# We could define our own intervals and both sides of number lines can be used and as well as starting and end things.
