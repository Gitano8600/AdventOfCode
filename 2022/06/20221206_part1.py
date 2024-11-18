import re

file = open("input.txt", "r")
value = file.read()

pattern = r'(?=(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.))'
match = re.search(pattern, value)

start_position = match.start() + 4

print(start_position)