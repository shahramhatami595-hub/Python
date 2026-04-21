Pay = float(input("Enter your fee:"))


if(Pay >= 500):

    print("You have discound!")
if (Pay < 500):
    vip = input("Are you a vip person ?").lower()
    if(vip == "yes"):
        print("you have discound!")
    else:
        print("Please pay it completely")

    
