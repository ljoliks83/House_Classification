# This function takes a string as input and returns the string with the first and last characters swapped.
def swap_first_last(string):
    # Write your code here
    temp_l = string[0]
    temp_r = string[-1]
    string = string.lstrip(temp_l)
    string = string.rstrip(temp_r)
    string = temp_r + string + temp_l
    return string

# Taking user's input
input_string = input()

# Invoking the function
result = swap_first_last(input_string)

# Printing the result
print(result)