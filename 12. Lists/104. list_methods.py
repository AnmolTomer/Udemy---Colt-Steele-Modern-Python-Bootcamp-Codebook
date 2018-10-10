first_list = [1,2,3,4]
first_list.insert(2,'Hi..!')
print(first_list)

items = ["socks", 'mug', "tea pot", "cat food"]
# items.clear()
#Lets the items list to be a list but clears everything within it.
items = ["socks", 'mug', "tea pot", "cat food"]
first_list.pop() # Remove the last element

first_list.pop(1) #Removes the element with the index 1

# While removing it also returns the item that is removed so that we may append or assign it somewhere else as well in case you want to capture and do some operation.
last_item = items.pop()
print(last_item)
# remove - Remove the first item from the list whose value is x.
names = ["Colt","Blue","Arya","Lena","Colt","Selena","Pablo"]
names.remove("Blue")
print(names)
print(names.count("Colt")) #Counts the number of times a particular value or string is present inside a list.
# Using join is commonly done to convert lists to strings
words = ['Coding', 'is', 'fun']
b = ' '.join(words)
print(b)
name = ["Mr", "Steele"]
c= '. '.join(name)
print(c)

friends = ["Colt","Blue","Arya","Lena","Colt","Selena","Pablo"]
d = ", ".join(friends)
print(d)