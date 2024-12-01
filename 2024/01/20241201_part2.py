file = open("input.txt", "r")
values = file.read().splitlines()
result = 0

left_numbers = []
right_numbers = []

for value in values:
    left_numbers.append(int(value.split('   ')[0]))
    right_numbers.append(int(value.split('   ')[1]))

for number in left_numbers:
    result += number * right_numbers.count(number)

print(result)
