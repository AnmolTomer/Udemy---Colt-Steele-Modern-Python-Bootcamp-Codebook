#Psuedo  Code: Ask for age
# 18-21 Wristband and No Drinks

# Method1
# age = input("How old are you: ")
# age = int(age)
# if age != "":
#     if age >= 18 and age < 21:
#         print("You can enter, but need a wristband ! Also no drinks for you ese!")
#         # 21+ Normal Entry and Drinks

#     elif age >= 21:
#         print("Your age is good to enter, and can drink!")
#         # else too young, sorry.

#     else:
#         print("You can't come in little one! :( ")
# else:
#     print("You drunk or what mate ? Enter a proper number as your age.")


#Now the problem is if the user hits empty string without an int and hits enter then Python throws an error.
#To solve that problem we sub-class all the statements about age inside a if != "" if not equal to empty string. Else enter valid age.
#For now just focusing on user hitting enter and not giving asljal0923 or something stupid as an input. We'll see about that in other videos.

age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You age good to enter, and can drink!")

    elif age >= 18:
        print("You can enter, but need a wristband ! Also no drinks for you ese!")

    else:
        print("You can't come in little one! :( ")
else:
    print("You drunk or what mate ? Enter a proper number as your age.")