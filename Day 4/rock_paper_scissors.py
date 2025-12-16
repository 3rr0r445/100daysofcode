import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to Rock, Paper, Scissors!")

images =[rock, paper, scissors]


user_choice = int(input("Enter a number between 0 and 2. Rock(0), Paper(1), or Scissors(2)? "))
    elif user_choice >= 3 or user_choice < 0:
        print("You typed an Invalid Number and instantly lose! Suck it!")

else:
    print(images[user_choice])

    cpu_choice = random.randint(0, 2)
    print(f"Computer Chose: ")
    print(images[cpu_choice])

if user_choice == 0 and cpu_choice == 2:
    print("You Win!")
    if cpu_choice == 0 and user_choice == 2:
        print("You Lose!")

    elif cpu_choice > user_choice:
        print("You Lose!")
    elif user_choice > cpu_choice:
        print("You win!")
    elif cpu_choice == user_choice:
        print("TIE!!!")

