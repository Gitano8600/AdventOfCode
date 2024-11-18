import re

file = open("input.txt", "r")
values = file.read().splitlines()
final_value = 0


for value in values:
    a, b, c, d = re.findall(r"[\w']+", value)
    if max(int(a), int(c)) <= min(int(b), int(d)):
        final_value += 1

print(final_value)
