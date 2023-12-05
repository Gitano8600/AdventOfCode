file = open("input.txt", "r")
values = file.read().splitlines()
result_value = None

seeds = []
seed_dict = dict()
maps = dict()
next_line_is_value = False
current_map_name = ""

for item in values:
    if item.startswith("seeds:"):

        seeds_list = item.split(": ")[1].split(" ")
        for i in range(len(seeds_list)):
            if i%2 == 0:
                seed_dict[int(seeds_list[i])] = int(seeds_list[i+1])

    if item == "":
        next_line_is_value = False

    if "map:" in item:
        next_line_is_value = True
        current_map_name = item[:-5]
        maps[current_map_name] = []

    elif next_line_is_value:
        raw_values = tuple(item.split(" "))
        val0 = int(raw_values[1])
        val1 = int(raw_values[1]) + int(raw_values[2]) -1
        val2 = int(raw_values[0]) - int(raw_values[1])
        relevant_values = (val0, val1, val2)

        maps[current_map_name].append(relevant_values)

for key, value in seed_dict.items():
    seeds.append(iter(range(key, key+value)))

for seed in seeds:
    for val in seed:
        actual_value = val
        for key in maps.keys():
            for item in maps[key]:
                if item[0] <= actual_value <= item[1]:
                    actual_value = actual_value + item[2]
                    break

        if result_value is None or result_value > actual_value:
            result_value = actual_value

print("result_value", result_value)
