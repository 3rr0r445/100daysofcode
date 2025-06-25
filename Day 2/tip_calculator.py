# Print introductory message
print("Welcome to the tip calculator.")

# Prompt user for bill total, convert it from a string to a float, and save it as variable bill
bill = float(input("What was the total bill? $"))

# Prompt user to input a percentage amount tip to use
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Prompt the user for the number of people splitting the bill
people = int(input("How many people to split the bill? "))

# Find the percentage amount by diving the tip by 100
tip_percentage = tip / 100

# Add percentage amount to the bill
bill_end = round(bill * tip_percentage, 2)

# Redefine bill variable to include the tip percentage
bill += bill_end

# Divide the total bill by the people paying
end_result = bill / people 

# Round the result to two digits and set as a last variable
rounded_result = round(end_result, 2)

# Print the result
print(rounded_result)
