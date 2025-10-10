#In this exercise, I'm going to prompt the user for their name and then
#I will calculate the number of characters in their answer. I will frame it in print functions to return the values to them.

#First, I'll use the input function for their name and save the response as a variable.

username = input("What is your name? ")

#Second, I'll use the len function on that variable to get the number of characters, and then save it as it's own variable.

length = len(username)

#Finally, I'll print the answer using the varible for the user to see.

#print("Your name has exactly " + length + " characters!")

#The code above resulted in an error. The problem was the variable 'length' is an integer
#You can only concatenate strings to strings, so You have to convert the integer to a string.

print("Your name has exactly " + str(length) + " characters!")


#You can also do it using no variables at all, which is how I was supposed to.
#I'm very good at overcomplicating things.

print(len(input("What is your name? ")))
#This is how I was supposed to do it, printing just the answer and nothing else.
