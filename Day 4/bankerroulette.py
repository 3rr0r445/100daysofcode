import random

names_string = input("Give me everyone's name seperated by a comma. ")

names = names_string.split(", ")
# random_name = random.choices(names)
# print(random_name)

number = len(names)
print(number)

answer = random.randint(0, number - 1)
print(names[answer])