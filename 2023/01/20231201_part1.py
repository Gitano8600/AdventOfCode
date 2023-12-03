
file = open("input.txt", "r")

values = file.read().splitlines()
int_values = []
int_values_rel = []

for item in values:
    temp_string = ""
    for char in item:
        if char.isdigit():
            temp_string += char
    int_values.append(temp_string)

for item in int_values:
    if len(item) < 2:
        int_values_rel.append(item + item)
    else:
        int_values_rel.append(item[0] + item[-1])

final_number = 0
for item in int_values_rel:
    final_number += int(item)

print(final_number)