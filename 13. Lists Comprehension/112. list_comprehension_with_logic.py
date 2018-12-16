numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num%2==0]
odds = [num for num in numbers if num%2 != 0]
print(evens)
print(odds)


a = [num*2 if num%2==0 else num/2 for num in numbers]
print(a)


# Basically taking the string with_vowels and removing all the vowels and then printing it again using iteration in one line only.
with_vowels = "This is so much fun"
without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
print(without_vowels)



# join is basically used to join all the elements of the list and '' defines what comes between 2 elements when we join those two together.

before_join = ['cool', 'dude']
joined = '___'.join(before_join)
print(joined)


answer = [val for val in range(1,101) if val%12==0]
print(answer)

with_vowels = "amazing"
without_vowels = ''.join(abc for abc in with_vowels if abc not in 'aeiou')
print(without_vowels)

answer = [[i for i in range(0,3)] for num in range(0,3)]
print(answer)