#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password_letters = random.sample(letters, nr_letters)
# password_symbols = random.sample(symbols, nr_symbols)
# password_numbers = random.sample(numbers, nr_numbers)

# password = password_letters + password_symbols + password_numbers
# combined = "".join(password)
# print(f"Your new password is {combined}")


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = password_letters + password_symbols + password_numbers
# shuffled_password = random.sample(combined, len(combined))
# combined = "".join(shuffled_password)
# print(f"Your new password is {combined}")

# # I googled up the random.sample as it hadn't been covered in the course. I'm fearing it wasn't the way she wanted us to do it.
# # She wrote out the logic herself instead of using a built in function.

#EASY
password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your new password is {password}")

#HARD

password_list = [

]
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    # OR password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)


#print(f"Your new password is {password_list}")
random.shuffle(password_list)
#print(f"Your new password is {password_list}")

password = ""
for char in password_list:
    password += char

print(f"Your FINAL password is {password}")