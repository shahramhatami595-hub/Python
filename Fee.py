user_name = ["Ali","Reza","Ahmad","Shahram","Jon","Bob","Jany"]

user_name_new = input("Enter your name:")

if (user_name_new in user_name):

    print("Login successful!")

if ( user_name_new not in user_name):

    if(len(user_name_new) > 3 ):
       
       user_name.append(user_name_new)
       
       print("Conguralate you added to the list!")

    else:
        print("Name is too short!")   

