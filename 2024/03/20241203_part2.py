import re


file = open("input.txt", "r")
value = file.read()
result = 0

selection_regex = r"(?:^|do\(\))([^d]+)|don't\(\)[^d]*"
instruction_regex = r"mul\((\d+,\d+)\)"

valid_sections = re.findall(selection_regex, value)
filtered_matches = []


for sequence in valid_sections:
    if sequence:  # Ensure it's a valid match
        filtered_matches.extend(re.findall(instruction_regex, sequence))


for pair in filtered_matches:
    x, y = pair.split(',')
    print('x,y', x, y)
    result += int(x) * int(y)

print(result)
