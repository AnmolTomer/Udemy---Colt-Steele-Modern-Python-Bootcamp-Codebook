age = 43
# 2-8 yo 2 dollar ticket
# 65+ yo 5 dollar ticket
#Others 10 dollar tickets
if not ((age >= 2 and age <= 8) or (age >= 65)):
    print("You pay $10 for ticket and are not a child or senior.")
else:
    print("You are a child or senior.")
# elif age >= 2 and age <= 8:
#     print("You pay $2 for ticket and are a child.")
# elif age >= 100:
#     print("You won't be around for long. Treat on us. You get a free entry old man :D ")
# else:
#     print("Age you idiot! Give us your age in years!")