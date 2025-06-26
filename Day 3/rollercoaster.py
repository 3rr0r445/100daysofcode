# Prompt user for height in cm
height = int(input("What is your height in cm? "))
# Set a variable for the bill and assign its default to 0
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    # Prompt user for age
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5 dollars.")
    elif age <= 18:
        bill = 7
        print("Your tickets are 7 dollars.")
    elif age >= 45 and age <=55:
        print("Everything is going to be okay. Ride for free.")
    else:
        bill = 12
        print("Adult tickets are 12 dollars.")
    
wants_photo = input("Do you want a photo taken? Y or N ")
if wants_photo == "Y":
    bill += 3


print(f"Your total is ${bill}.")

