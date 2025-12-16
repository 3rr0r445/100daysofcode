#The objective of this exercise is to take a two digit number and have the code add the two digits together
#since numbers are integers, it will involve changing the data types

#First, let's go ahead and prompt the user for a two digit number.

number = input("Give me a two digit number ")

#User input is automatically assigned to a string datatype. I overcomplicated earlier and was trying to convert it.

#Assign variables to each digit of the number, converting them to integers as you do.

first = int(number[0])
second = int(number[1])

#Assign a variable to the answer to the equation, with our new integers.
answer = first + second

#print the answer using a formated string, or fstring
print(f"{first} + {second} = {answer}")

