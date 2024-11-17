file = open("input.txt", "r")
values = file.read().splitlines()

current_calories = 0
list_of_calories = []

for value in values:
    if value != '':
        current_calories += int(value)
    else:
        list_of_calories.append(current_calories)
        current_calories = 0

list_of_calories.sort(reverse=True)

print(list_of_calories[0]+list_of_calories[1]+list_of_calories[2])


        