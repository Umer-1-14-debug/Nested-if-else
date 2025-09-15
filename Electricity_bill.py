units=int(input("Enter your units."))
bill=0
if units>=50:
    bill=25
    print("The bill is ",bill)
elif units>=100:
    bill=35
    print("The bill is ",bill)
elif units>=200:
    bill=45
    print("The bill is ",bill)
else:
    bill=60
    print("The bill is ",bill)