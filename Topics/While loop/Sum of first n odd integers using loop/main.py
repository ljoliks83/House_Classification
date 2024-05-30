# Read a number from the user
n = int(input())

# Initialize variables
sum = 0
current_odd = 1
counter = 1

# TODO: Write a while loop that calculates the sum of the first n positive odd integers
# Hint: In each iteration, add the current odd number to the sum and update the current odd number

while counter <= n:
    sum += current_odd
    current_odd += 2
    counter += 1

# Print the sum
print(sum)