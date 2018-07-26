from django.template.defaultfilters import upper, lower
#  If you get the following error :
# --------------------------------------------------------------------
# Traceback (most recent call last):
#   File "Strings.py", line 1, in <module>
#     from django.template.defaultfilters import upper, lower
# ModuleNotFoundError: No module named 'django'
#  -------------------------------------------------------------------
#  Then start cmd prompt with adming rights and type in pip install django. Wait for it to get installed and then try running this again.
# It means that from library django.whatever it imports fxn upper
name = "CosmicC"
Strlen = len(name)
# find length of string.
print(Strlen)
print(upper(name))
print(lower(name))
print(name)
#  Tasks done 1. Import library 2. Use fxn of that lib
# 3. Use that while printing output. Remember to follow IPO always.
title = "Your Grade is {}" .format(79)
print(title)
str1 = "San Fransisco"
str2 = " is good...!!"
print(str1 + str2)  # String Concatenation
str3 = "San Fransisco{}".format(" is good...!!")
print(str3)
# 2 methods to combine strings.