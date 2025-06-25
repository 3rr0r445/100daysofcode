height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# Convert the data types to float and integer rather than strings
height = float(height)
weight = float(weight)

# Done with the exponent operator **, very handy.
# bmi = weight / height ** 2

# Originally tried to do like this (bmi = weight / height ** height)
# The math wasn't mathing. I needed to put the height operation in ()

bmi = (round(weight / height ** 2))

# Convert the result into an integet and print it to screen
print (int(bmi))


# Use conditional statements to determine the bmi definition
if bmi >= 35:
    print("You are clinically obese!")
elif bmi > 30 and bmi < 35:
    print("You are obese!")
elif bmi > 25 and bmi < 30:
    print("You are overweight!")
elif bmi > 18.5 and bmi < 25:
    print("You have a normal weight!")
else:
    print("You are underweight!")



# Convert to Imperial instead of Metric? Freedom Units?

