integer1 = int(input("Please enter the day in the form of a 2 digit integer"))
integer2 = int(input("Please enter  the month in the form of a 2 digit integer"))
integer3 = int(input("Please enter an the year in the form of a 2 digit integer"))


if integer2 == 1:
    month = "January"
elif integer2 == 2:
    month = "February"
elif integer2 == 3:
    month ="March"
elif integer2 == 4:
    month = "April"
elif integer2 == 5:
    month = "May"
elif integer2 == 6:
    month = "June"
elif integer2 ==7:
    month = "July"
elif integer2 == 8:
    month = "August"
elif integer2 == 9:
    month = "September"
elif integer2 == 10:
    month = "October"
elif integer2 == 11:
    month = "November"
elif integer2 == 12:
    month = "December"

print("The date is the {0}{1} of {2} 20{3}".format(integer1,,month,integer3))
                    
