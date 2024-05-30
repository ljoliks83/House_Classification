word = input()
number_of_spaces = int(input())

word = list(word)
print(*word, sep=' ' * number_of_spaces)
