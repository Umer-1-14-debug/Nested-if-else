yes_or_no=input("Do you have any medical clause. ")
attendence=int(input("Enter your attendence."))
if yes_or_no=="yes":
    if attendence<=75:
        print("You can give the exam.")
    else:
        print("You cannot give the exam.")
else:
    print("You cannot give the exam.")