#  Two types of loops we will focus on for and while loop. We can use these in different ways.
#  Syntax, quirks and use cases of for loops.
#  Conceptualising the idea...We have a collection of data and something we could iterate over like lists or string and we could loop for every
#  character in string or number in range or item in list.
#  String, List and Range are 3 things we could loop over.
# for item in iterable_object:
    #  do something with the item.
#  Iterable object is the collection of the data that was shown and item is what we want to call the initiator.
#  Item references our current position of the iterator within the iterable. Item iterates over or runs through every item of the collection
#  and then goes away when it has been looped enough times and it has server its purpose.
# for char in "hello":
    # we are working with string hello and for loop and char represents a single character and if we do print char and it goes till the end.
#  Whatever this char or single variable is called it represents the single part of the iterable collection and is constantly updated
#  Until the end of the loop is hit.

#  for loops with ranges:
#  Let's print numbers 1-7 using our knowledge of  looping thru ranges.
#  Range is a way of quickly generating numbers in a range.
# for number in range(1,8):
#     print(number)
    #  With syntax above each time through the loop everything below just like a conditional 

# for x in range(1,10):
#     print(x)
#     print(x*x)

#  Let's work with a string

# for char in "coffee":
#     print(char*10)

#  Iterable Collection, range, string, individual number or printing whatever is there in the variable.
# for num in "122434":
#     print(num)