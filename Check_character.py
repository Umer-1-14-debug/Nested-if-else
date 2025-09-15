character=input("Please enter a character number or symbol")
if (character>="a" and character<="z"):
    print("This is an alphabet")
elif (character>="0" and character<="9"):
    print("This is a number")
else:
    print("This is a symbol")