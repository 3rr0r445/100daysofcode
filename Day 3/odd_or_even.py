# Prompt user for a number to check whether odd or even
number = int(input("What number do you want to check? "))

# See if divided by 2, the number has any remainder and print answer accordingly
if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")


          