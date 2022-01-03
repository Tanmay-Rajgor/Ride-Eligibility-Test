height = int(input("Enter Your Height in Centimeter : "))
if height > 120:
    print("Can Ride")
    age = int(input("Enter Your Age : "))
    if age > 18:
        print("You need to pay $10 for ride. because you are over 18.")
    elif age > 12 and age < 18:
        print("You need to pay $7 for ride. because you are between 12 - 18 age group.") 
    else:
        print("You need to pay $5 for ride.")        
else:
    print("Can't Ride")    