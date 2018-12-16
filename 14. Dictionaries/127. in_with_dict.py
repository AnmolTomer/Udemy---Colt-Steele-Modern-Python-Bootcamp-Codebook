instructor = {
    "name":"Cosmic",
    "num_courses":'4',
    "favorite_language" :"Python",
    "is_hillarious": False,
    44 : "is my favorite number"

}

# Way to check if a key exists in a dict and returns True or False as a response
a = "name" in instructor
print(a)
b = "phone" in instructor
print(b)
c = instructor.values()
print(c)

#  Direct in goes to find the given stuff in the key of dictionary if you want otherwise then you should go for .values() method defined above.
