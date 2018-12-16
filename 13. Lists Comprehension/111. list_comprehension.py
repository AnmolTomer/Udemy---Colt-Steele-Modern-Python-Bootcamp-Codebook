"""
Applies to many other data structures dictionaries and things like tuples and generators all of which we will see later.
Understanding these is imp.
Cool shorthand which allows us to make new lists that are direct copies of other lists or are tweaked version of source list.

Syntax : Syntax is bizzare but try to understand as I explain line by line
Sq. Brackets []
then var_name for var_name which remains same so we have now [var_name for var_name in (name_of_other_list or range)]
[___ for ____ in list]

"""

nums = [1,2,3]
print(nums)
a = [x*10 for x in nums]
print(a)
a = [x/2 for x in nums]
print(a)
# Taking an existing list and making a new list with initial list as the source list.

#Doing the same with a loop
numbers = [1,2,3,4,5]
doubled_numbers = []
for num in numbers:
    doubled_number = num*2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)
comp_l = list((d)*2 for d in numbers)
print(comp_l)

name = 'cosmic'
b = [char.upper() for char in name]
print(b)

friends = ['ross','pheobe','joey','monica','chandler']
c = [friend.upper() for friend in friends]
print(c)

d = [num*10 for num in range(1,6)]
print(d)

f = [1,2,3,4,5]
string_list = [str(numb) for numb in f]
print(string_list)

e = [bool(val) for val in [0,1,[],'']]
print(e)

colors = ['red', 'orange', 'green', 'yellow', 'blue']
g = [color.upper() for color in colors]
print(g)

numb = [1,2,3]
h = [str(numba)+"_Generated_By_COSMIC" for numba in numb]
print(h)


