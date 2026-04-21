import random
number = random.randint(1,100)
if(number == 0):
    print("Zero")
elif ( number % 2 == 0):
    print("Even")
else:
    print("Odd")