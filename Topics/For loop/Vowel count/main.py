string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0
i = 0

for _ in string:
    if string[i] in vowels:
        counter += 1
    i += 1

print(counter)
