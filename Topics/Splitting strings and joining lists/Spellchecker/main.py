dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

input_string = input()
input_list = input_string.split()

counter = 0

for i in range(len(input_list)):
    if input_list[i] not in dictionary:
        print(input_list[i])
        counter += 1

if counter == 0:
    print("OK")