total_sum = 0

with open("numbers.txt", 'r') as file:
    for line in file:
        number = int(line[:-1])
        total_sum += number

print(total_sum)