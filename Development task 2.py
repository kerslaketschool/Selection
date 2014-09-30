temp = int(input("Please enter your water temperature in centigrade"))

if temp <= 0:
    print("Your water is frozen")
elif temp > 99:
    print ("Your water is boiling!")
else:
    print("Your water is at room temperature")
