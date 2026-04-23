guests = ["sara","samim","shahram","alis","hadi","quasim"]
name = input("What is your name?").lower()
Age = int(input("How old are you?"))

if (name in guests and Age > 18):
    print("Welcome you are invited!")
elif(name in guests and Age <= 18):
    print("You are too yong for this event!")
else:
    print("You are not in the list!")