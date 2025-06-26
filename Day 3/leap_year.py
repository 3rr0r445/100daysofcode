# Prompt user for a year, converting it to an integer and setting it as the variable year
year = int(input("What year would you like to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year!")
        else:
            print("Not a leap year")
    else:
        print("This is a leap year")
else:
    print("Not a leap year")