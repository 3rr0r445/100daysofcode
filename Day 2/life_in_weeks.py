# Prompt user for their age and compare to max age (90)
age = int(input("What is your current age? "))
max_age = 90
answer_age = max_age - age

# Define variables for months, weeks, days using mathmatical operators
answer_months = answer_age * 12
answer_weeks = answer_age * 52
answer_days = answer_age * 365

# Print the results using an F-String
print(f"You have {answer_days} days, {answer_weeks} weeks, and {answer_months} months left.")

