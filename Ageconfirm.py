Fee = float(input("Enter your fee: "))

persantage_over500 = (20 * Fee)/100

total_over500 = Fee - persantage_over500

persantage_over200 = (10 * Fee)/100

total_over200 = Fee - persantage_over200

if ( Fee > 500):

    print(f"Your total fee is: {total_over500}$")

elif(Fee >= 200 and Fee <= 500):

    print(f"Your total fee is:{total_over200}$")
    
else:
    print(f"Your total fee is:{Fee}$")


