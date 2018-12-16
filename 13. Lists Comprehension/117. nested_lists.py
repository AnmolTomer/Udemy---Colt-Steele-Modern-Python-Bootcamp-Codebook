nested_list = [[1,2,3],[4,5,6],[7,8,9]]

#Using nested list with 2 loops to print all the elements.
for l in nested_list:
    for val in l:
        print(val)

coords = [[10.423,9.132],[37.212,-14.092],[21.367,32.572]]
for loc in coords:
    for prop in loc:
        print(prop)

# Above we saw how to use nested loops to print the elements of nested lists.

# As nested loop is a thing, so do we have nested list comprehensions as well.
[[print(val) for val in l]for l in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

d = [['X' if num%2 != 0 else "O" for num in range(1,4)]for val in range(1,4)]
print(d)

# A grid of 3*3 of *
e = [["*" for val in range(1,4)] for p in range(1,4)]
print(e)