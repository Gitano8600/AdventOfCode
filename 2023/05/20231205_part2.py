import time

start = time.time()
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
seed_dict = dict()
maps = dict()
next_line_is_value = False
current_map_name = ""

for item in values:
    if item.startswith("seeds:"):

        seeds_list = item.split(": ")[1].split(" ")
        print("seeds list", seeds_list)
        print("length_seed_list", len(seeds_list))
        for i in range(len(seeds_list)):
            if i%2 == 0:
                seed_dict[int(seeds_list[i])] = int(seeds_list[i+1])

    if item == "":
        next_line_is_value = False
    if "map:" in item:
        print(item[:-5])
        next_line_is_value = True
        current_map_name = item[:-5]
        maps[current_map_name] = []
    elif next_line_is_value:
        raw_values = tuple(item.split(" "))
        print("raw_values", raw_values)
        val0 = int(raw_values[1])
        val1 = int(raw_values[1]) + int(raw_values[2]) -1
        val2 = int(raw_values[0]) - int(raw_values[1])
        print("vals", val0, val1, val2)
        relevant_values = (val0, val1, val2)

        maps[current_map_name].append(relevant_values)

print("seed_dict", seed_dict)
for key, value in seed_dict.items():
    seeds.append(iter(range(key, key+value)))

print("seeds", seeds)

print("maps", maps)

for seed in seeds:
    temp_time = time.time()
    print("The time of elapsed execution of above program is :", (temp_time - start) * 10 ** 3, "ms")

    for val in seed:

        actual_value = val
        for key in maps.keys():
            for item in maps[key]:

                if item[0] <= actual_value <= item[1]:

                    actual_value = actual_value + item[2]
                    break


        if result_value is None or result_value > actual_value:
            result_value = actual_value

print("Seeds", seeds)
print("Maps", maps)
print(values)
print("result_value", result_value)
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")