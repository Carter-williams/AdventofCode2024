input = open("C:/Users/willic130/Downloads/AOCd1input.txt", 'r')

input_list = input.readlines()

first_list = []
second_list = []

for line in input_list:
    to_add = line.split()
    first_list.append(int(to_add[0]))
    second_list.append(int(to_add[1]))

first_list.sort()
second_list.sort()

total = 0

for i in range(len(first_list)):
    total += abs(first_list[i] - second_list[i])

print(total)

similarity_score = 0

for i in range(len(first_list)):
    x = first_list[i]
    similarity_score += x * second_list.count(x)

print(similarity_score)
    