file = open("input.txt", "r")
values = file.read().splitlines()
result_value = 0

time = int("".join(values[0].split()[1:]))
distance = int("".join(values[1].split()[1:]))

for var in range(time):
    if (time-var) * var > distance:
        result_value += 1

print(result_value)