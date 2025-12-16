student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


#Find the average of the student heights to the nearest whole number
#Do NOT use the len or sum functions, that would make it too easy. Use loops

# Use a for loop to increase a number for each item in the list to find the length of list items
list_len = 0
for n in student_heights:
    list_len += 1
print(f"The number of heights is {list_len}!")

#Use a for loop to add each item to a total, or sum of all heights. 
sum = 0
for n in student_heights:
    sum += n
print(f"The total sum of heights is {sum}!")

#Find the average using base division to round it to the nearest whole number, as so not to use the round function

average = sum // list_len

print(f"The average height is {average}!")

