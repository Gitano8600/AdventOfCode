import re

file = open("input.txt", "r")
values = file.read()
final_value = 0
regexp = re.compile(r'[=]')
boxes = dict()

for i in range(256):
    boxes[i] = dict()


def hash_string(hash_str, n=0):
    new_value = (ord(hash_str[0])+n) * 17 % 256
    if len(hash_str) == 1:
        return new_value
    else:
        return hash_string(hash_str[1:], new_value)


for value in values.split(","):
    print("value", value)
    if regexp.search(value):
        box = hash_string(value.split("=")[0])
        boxes[box][value.split("=")[0]] = int(value[-1])
        print(boxes)
    else:
        try:
            del boxes[hash_string(value[:-1])][value[:-1]]
            print(boxes)
        except:
            continue

for key, value in boxes.items():
    pos = 1
    for key2, value2 in value.items():
        final_value += (key + 1) * pos * value2
        pos += 1

print(final_value)
