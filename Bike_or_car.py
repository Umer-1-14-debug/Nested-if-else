print("You want to go with a car or bike.")
print("1). Bike")
print("2). Car")
choose=int(input("Choose from which you want to go."))
if choose==1:
    print("What type of bike do you want to choose.")
    print("1).Scooti")
    print("2).Scooter")
    choose01=int(input("Choose the type of bike."))
    if choose01==1:
        print("So your choice is scooti.")
    else:
        print("So your choice is scooter.")
elif choose==2:
    print("What type of car do you want to choose.")
    print("1).Sadan")
    print("2).SUV")
    choose01=int(input("Choose the type of car."))
    if choose01==1:
        print("So your choice is Sadan.")
    else:
        print("So your choice is SUV.")
else:
    print("Invalid number.")