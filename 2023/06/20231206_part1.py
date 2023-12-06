file = open("input.txt", "r")
values = file.read().splitlines()
result_value = 0

time = tuple(int(num) for num in values[0].split()[1:])
distance = tuple(int(num) for num in values[1].split()[1:])

for idx, value in enumerate(time):
    temp_value = 0
    for var in range(value):
        if (time[idx] - var) * (var) > distance[idx]:
            temp_value += 1

    result_value = result_value + temp_value if result_value == 0 else result_value * temp_value

print(result_value)
