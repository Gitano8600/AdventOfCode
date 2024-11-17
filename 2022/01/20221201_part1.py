file = open("input.txt", "r")
values = file.read().splitlines()

current_calories = 0
highest_calories = 0

for value in values:
    if value != '':
        current_calories += int(value)
    else:
        if current_calories > highest_calories:
            highest_calories = current_calories
        current_calories = 0

if current_calories > highest_calories:
    highest_calories = current_calories

print(highest_calories)


