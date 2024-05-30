dictionary = ["https://", "http://", "www."]

text = input()
words = text.split()
for word in words:
    # finish the code here
    for i in range(len(dictionary)):
        if word.lower().startswith(dictionary[i]):
            print(word)