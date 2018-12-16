# Limitation of list is that it stores type of data of one kind. We are not able to conclude what is each element referring to in the list .
# Things get weird if we want to make something like  for one data element more than one info that we want to share.
# To describe data in more detail we lean towards dictionary.
# Dictionary consists of key:value pairs. Key to describe the data and value of the data.
# In dict we decide how we want to store the data and under what key is the data stored.
instructor = {"name":"Cosmic","num_courses":'4',"favorite_language" :"Python","is_hillarious": False, 44 : "is my favorite number"}
cat = {'name':'Blue','age':3.5, "isCute":True}
print(cat)
print(instructor)
cat2 = dict(name = 'Kitty',age = 3.5, farts = True, isAggressive = True)
print(cat2)
