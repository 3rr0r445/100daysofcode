# Prompt the user for a two digit number
# Convert each digit into integers and add them together
# Print the result in it's own variable


two_digit_number = input("Type a two digit number: ")

answer = (int(two_digit_number[0]) + int(two_digit_number[1]))
print(answer)