# Print Welcome Prompt
print("Welcome to my love calculator!")
# Prompt user for their name and their love interests name, saving them at variables name1 and name2
name1 = input("What is your full name? ")
name2 = input("What is their full name? ")

# Create a
combined_names = name1 + name2
lower_combined_names = combined_names.lower()

t = lower_combined_names.count("t")
r = lower_combined_names.count("r")
u = lower_combined_names.count("u")
e = lower_combined_names.count("e")

true = t + r + u + e

l = lower_combined_names.count("l")
o = lower_combined_names.count("o")
v = lower_combined_names.count("v")
e = lower_combined_names.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}. You go together like Coke and Mentos.")
elif (love_score >= 40) or (love_score <=50):
    print(f"Your love score is {love_score}. You are alright together.")
else:
    print(f"Your love score is {love_score}.")





