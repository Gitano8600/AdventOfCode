file = open("input.txt", "r")
values = file.read().splitlines()
result_value = None

seeds = []
maps = dict()
next_line_is_value = False
current_map_name = ""

for item in values:

    if item.startswith("seeds:"):
        for seed in item.split(": ")[1].split(" "):
            seeds.append(int(seed))

    if item == "":
        next_line_is_value = False

    if "map:" in item:
        print(item[:-5])
        next_line_is_value = True
        current_map_name = item[:-5]
        maps[current_map_name] = []

    elif next_line_is_value:
        relevant_values = [eval(i) for i in item.split(" ")]
        maps[current_map_name].append(relevant_values)

for seed in seeds:
    actual_value = seed
    for key in maps.keys():
        for item in maps[key]:
            if item[1] <= actual_value <= (item[1] + item[2] - 1):
                actual_value = actual_value + (item[0] - item[1])
                break

    if result_value is None or result_value > actual_value:
        result_value = actual_value

print("result_value", result_value)
