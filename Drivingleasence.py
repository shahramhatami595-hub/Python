text1 = input("Enter some text: ")

text2 = input("Enter some text: ")

if (len(text1) > len(text2)):

    print("The first text is longer than the second one ")

elif(len(text2)>len(text1)):

    print("The secound text is longer than the first one ")
    
else:
    print("Two text are equals")