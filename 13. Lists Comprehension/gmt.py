
day = input().rstrip()
hours = int(input())
minute = int(input())
if ((hours < 0) or (minute < 0) or (hours>24) or (minute>60)) :
    print("Invalid Input")
else:
    min_to_add = 60*5+30 # i.e. 5 hours and 30 minutes
    num_of_hours = (hours+5+(30+minute))//60
    minute += min_to_add
    minute = minute%60
    if num_of_hours > 24:
        num_of_hours = num_of_hours-24
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        for i in range(len(days)):
            if days[i]==day:
                print(days[i+1])