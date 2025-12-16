import random

rock = 1
paper = 2
scissors = 3

print("Rock. Paper. Scissors. You know how it works.")
print()
print()
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice = int(input("Choose a number: 1(rock), 2(paper), or 3(scissors)  "))
cpu_choice = random.randint(0, 2)

if user_choice == 1:
    if cpu_choice == 1:
        print("You Chose Rock.")
        print("CPU Chose Rock")
        print("TIE!")
    elif cpu_choice == 2:
        print("You Chose Rock")
        print("CPU Chose Paper")
        print("CPU WINS!")
    elif cpu_choice == 3:
        print("You Chose Rock")
        print("CPU Chose Scissors")
        print("")
    