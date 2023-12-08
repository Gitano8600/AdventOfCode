from collections import OrderedDict

file = open("input.txt", "r")
values = file.read().splitlines()
node_map = OrderedDict()
result_value = 0

for i in values[2:]:
    node_map[i[:3]] = (i[7:10], i[12:15])

curr_waypoint = "AAA"

while curr_waypoint != "ZZZ":
    for char in values[0]:
        curr_waypoint = node_map[curr_waypoint][1] if char == "R" else node_map[curr_waypoint][0]
        result_value += 1

print(result_value)
