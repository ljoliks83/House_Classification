percent = 1.071
init_sum = 0
years_count = 0

while not (50000 <= init_sum <= 700000):
#    print("Test input:")
    init_sum = int(input())

actual_sum = init_sum
#print("Test input:")
#print(actual_sum)

while actual_sum <= 700000:
    actual_sum = actual_sum * percent
    years_count += 1

#print("Correct output:")
print(years_count)
