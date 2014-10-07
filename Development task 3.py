#Toby Kerslake
#07-10-14
#Development excercise 3

hours = int(input("How many hours have you worked this week?"))
payRate = float(input("What is your hourly pay rate in pounds sterling"))

if hours < 0 or hours > 60:
    print("Invalid. Please enter a number between 0 and 60!")
elif hours > 40:
    finalPay = (payRate * 40) * ((hours * 40) * (payRate * 1.5))
    print("You have earned £{0} this week".format(finalPay))
else:
    finalPay = hours * payRate
    print("You have earned £{0} this week".format(finalPay))
