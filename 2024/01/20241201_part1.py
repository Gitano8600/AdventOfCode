file = open("input.txt", "r")
values = file.read().splitlines()
result = 0

left_numbers = []
right_numbers = []

for value in values:
    left_numbers.append(int(value.split('   ')[0]))
    right_numbers.append(int(value.split('   ')[1]))

left_numbers.sort()
right_numbers.sort()

for index, number in enumerate(left_numbers):
    result += abs(number-right_numbers[index])

print(result)
