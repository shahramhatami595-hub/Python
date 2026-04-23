Age = int(input("Please enter your age:"))

if(Age <= 0):

    print("Invalid input!")

elif(Age < 13):

    print("You are a child!")

elif(Age >= 13 and Age <= 19):

    print("You are teenger!")

elif(Age >= 20 and Age <= 64):

    print("You are adult!")

else:
    
    print("You are senior!")