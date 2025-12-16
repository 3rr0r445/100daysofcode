student_scores = input("Input a list of student scores. ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Starting Code Above. Do Not Code Above This Line!!

# Write a program that calculates the highest value in the list
# Do not use the max function to do it easily. 
# Probably will use a loop and conditionals.

max_value = student_scores[0]

# No conditionals. Just a for loop. This one uses list slicing
# It sets the default value for max_value as the first value in the list
# It uses list slicing to start iterating at the second list item
for n in student_scores[1:]:
    if n > max_value:
        max_value = n
print(f"The highest score in the class is {max_value}!")

# This one doesn't use list slicing, just the entire list.
for n in student_scores:
    if n > max_value:
        max_value = n

print(f"The highest score in the class is {max_value}!")