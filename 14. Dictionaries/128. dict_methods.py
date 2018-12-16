instructor = {
    "name":"Cosmic",
    "num_courses":'4',
    "favorite_language" :"Python",
    "is_hillarious": False,
    44 : "is my favorite number"

}

#  clear : clears all they keys and assigned values in the dictionary
""" a = instructor.clear()
print(a)
print(instructor)
 """

#  copy : Makes a copy of the dictionary instead of pointing. Default assigning a variable to the name of a dictionary actually keeps the values same 
#  in memory location and all it does is that it points and a new dict is not made. That's why we use copy. Much like [:] in lists.
""" inst_copy = instructor.copy() # Copying
print(inst_copy is instructor) #Expected O/p = False
a = inst_copy # Assigning and pointing to memory location of inst_copy Expected O/p = True
print(a is inst_copy)
print(a is instructor) """ # Expected O/p = True
#  is checks for memory location of objects to verify if they are actually equal. == checks for their values equality.

#  fromkeys : Called on an empty dictionary.

""" i = {}.fromkeys("a","b")
h = {}.fromkeys(['email'], 'unknown')
g = {}.fromkeys("a",[1,2,3,4,5]) """
#  We pass in an iterable collection  say a list with string email and value is passed then here it is unknown.
# Assigns value unknown to the key email 
""" j = {}.fromkeys("a",[1,2,3,4,5])
print(j) """
#  Used whenever we have lots and lots of keys and we want to set them to a default value. BTW dict and {} same
#  Used to create empty dictionaries with default values to initialise default values.
""" new_user = {}.fromkeys(['name','score','email','profile'],'unknown')
print(new_user)
new_user= new_user.fromkeys(['phone'],'unknown')
print(new_user) """


#  get : Retrieves a key in an object and return None instead of KeyError if the key does not exist.
d = dict(a=1,b=2,c=3)
print(d)

d["a"]
print(d.get("a"))
d["b"]
print(d.get("b"))
d["c"]
print(d.get("c"))
d["test_call"]
print(d.get("test_call"))
