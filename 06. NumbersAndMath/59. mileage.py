print("How many kilometers did you run today ?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"Your {kms} km ride is equal to {miles} miles." )
#round(thing to round, places to round to)
#we can do {round(miles, 2)} . Inside {} curly braces we can do math or whatever logic we want.