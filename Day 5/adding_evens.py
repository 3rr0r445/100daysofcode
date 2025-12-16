# Use everything you've learned so far to add only the even numbers between 1 and 100
# Include 1 and 100.
# It's probably going to take conditionals and will DEFINITELY use loops.

answer = 0

for i in range(1, 101):
    if i % 2 == 0:
        answer += i
print(answer) 