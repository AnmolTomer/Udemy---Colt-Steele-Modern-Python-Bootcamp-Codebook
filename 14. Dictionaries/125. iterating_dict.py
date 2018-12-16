instructor = {
    "name":"Cosmic",
    "num_courses":'4',
    "favorite_language" :"Python",
    "is_hillarious": False,
    44 : "is my favorite number"

}

#  Accessing all values in a dictionary
#  We'll loop through keys, loop through values, loop through both keys and values

# Values Print .values() method call on a dictionary
for value in instructor.values():
    print(value)

#  Keys print

for key in instructor.keys(): # .keys() method call on a dictionary
    print(key)

#  .items() is the method we call on the dictionary to print both the key as well as values pair

#  Method 1
"""b = instructor.items()
print(b)
"""

#  Method 2
"""for item in instructor.items():
    print(item)"""

#  Method 3
for key,value in instructor.items():
    print(f"key is {key} and value is {value}")

#  Exercise 126
# Loop over donations, add all the VALUES together and store in a variable called total_donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# Method 1
total_donations = []
# for donation in donations.values():
#     total_donations.append(donation)

# print(total_donations)
# print(sum(total_donations))

#  Method -2 
a = sum(donation for donation in donations.values())
print(a)

#  Method-3
b =  sum(donations.values())
print(b)