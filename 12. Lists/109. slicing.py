# Slicing --> some_list[start:stop:step]
#  Start stop step being the indexes of the list on which we want to perform the operation.
first_list = [1,2,3,4]
first_list[1:] #From one till end
first_list[3:] #From 3 till end
# If you enter a negative number as the start point of the slice then it will give that many numbers or items of the list from the end.
colors = ['violet', 'indigo', 'blue','green','yellow','orange','red']
colors[2] #Index element 2 i.e. yellow
#  Slicing
colors[2:] #Slicing from and including the element at index number 2.
#  To make a copy of the list just slice it from the starting or the none position that is either [0:] or do [:]
colors2 = colors[:] #Makes a duplicate of the colors in the name and new memory location of colors2.

