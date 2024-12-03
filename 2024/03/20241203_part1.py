import re


file = open("input.txt", "r")
value = file.read()
result = 0
regex_pattern = '(?<=mul\()(\d*,\d*)(?=\))'


for pair in re.finditer(regex_pattern, value):
    x, y = pair.group().split(',')
    result += int(x) * int(y)

print(result)
