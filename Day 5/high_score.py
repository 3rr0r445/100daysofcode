student_scores = input("Input a list of student scores. ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Starting Code Above. Do Not Code Above This Line!!

# Write a program that calculates the highest value in the list
# Do not use the max function to do it easily. 
# Probably will use a loop and conditionals.

max_value = student_scores[0]

# No conditionals. Just a for loop.
for n in student_scores[1:]:
    if n > max_value:
        max_value = n
    print(max_value)