import re

file = open("input.txt", "r")
value = file.read()
solution = '?'


for i, char in enumerate(value):
    if len(set(value[i:i+14])) == 14:
        solution = i+14
        break


print(solution)
