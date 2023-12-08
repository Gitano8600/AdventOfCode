from itertools import cycle
from math import lcm

file = open("input.txt", "r")
values = file.read().splitlines()


node_map = {i[:3]: (i[7:10], i[12:15]) for i in values[2:]}
starting_nodes = [i[:3] for i in values[2:] if i[2] == "A"]
paths = cycle(c=="R" for c in values[0])
steps = 0


def steps_to_goal(node):
    end_point = lambda waypoint: waypoint[2] == "Z"
    steps = 0
    while not end_point(node):
        node = node_map[node][next(paths)]
        steps += 1
    return steps


result_value = lcm(*(steps_to_goal(node) for node in starting_nodes))

print(result_value)
