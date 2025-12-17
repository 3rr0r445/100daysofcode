# Gonna print out numbers between 1 and 100.
# if the number is divisible by 3, instead print "fizz"
# if the number is divisible by 5, instead print "buzz"
# if the number is divisible by 3 and 5, instead print "Fizzbuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)