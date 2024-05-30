count = 0
sum = 0
i = 0

while i != 55:
    i = int(input())
    if i != 55:
        count += 1
        sum += i
    else:
        print(count)
        print(sum)
        print(round(sum/count))