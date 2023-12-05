file = open("input.txt", "r")
values = file.read().splitlines()
result_value = None

xvalues =[
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4"
]

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
        relevant_values = [eval(i) for i in item.split(" ")] #item.split(" ")
        #dest_range = int(relevant_values[0])
        #source_range = int(relevant_values[1])
        #range_length = int(relevant_values[2])
        maps[current_map_name].append(relevant_values)
        #print(dest_range, source_range, range_length)
        #for val in range(source_range, (source_range+range_length)):
        #    maps[current_map_name][int(val)] = dest_range
        #    dest_range += 1

for seed in seeds:
    #print("seed", seed)
    actual_value = seed
    for key in maps.keys():
        for item in maps[key]:
            #print("item", item)
            #print("start", item[1])
            #print("end", item[1] + item[2])
            #print("range", range(item[1], item[1] + item[2]))
            #print('actual_val_bef_loop', actual_value)
            if item[1] <= actual_value <= (item[1] + item[2] - 1):
                #print("loop hit")
                actual_value = actual_value + (item[0] - item[1])
                break
                #if item[1] > item[0]:
                #    actual_value = actual_value - item[0]
                #    break
                #elif item[1] < item[0]:
                #    actual_value = actual_value + item[0]
                #    break
            #print('actual_val_after_loop', actual_value)

        #if actual_value in maps[key].keys():
        #    actual_value = maps[key][actual_value]

    if result_value is None or result_value > actual_value:
        result_value = actual_value

print("Seeds", seeds)
print("Maps", maps)
print(values)
print("result_value", result_value)
