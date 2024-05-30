initial_amount = int(input())
final_quantity = int(input())
counter = 0
amount = initial_amount

while amount >= final_quantity:
    amount /= 2
    counter += 1

print(counter * 12)
