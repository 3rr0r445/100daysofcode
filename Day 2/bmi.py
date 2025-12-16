height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# Convert the data types to float and integer rather than strings
height = float(height)
weight = int(weight)

# Done with the exponent operator **, very handy.
# bmi = weight / height ** 2

# Originally tried to do like this (bmi = weight / height ** height)
# The math wasn't mathing. I needed to put the height operation in ()

bmi = weight / (height * height)

# Convert the result into an integer and print it to screen
print (int(bmi))

# Convert to Imperial instead of Metric? Freedom Units?

