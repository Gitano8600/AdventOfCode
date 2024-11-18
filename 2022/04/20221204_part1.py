import re

file = open("input.txt", "r")
values = file.read().splitlines()
final_value = 0


for value in values:
    a, b, c, d = re.findall(r"[\w']+", value)
    print(a, b, c, d)
    if int(a) < int(c):
        if int(b) >= int(d):
            print('hit1')
            final_value += 1
    elif int(c) < int(a):
        if int(d) >= int(b):
            print('hit2')
            final_value += 1
    elif int(a) == int(c):
        if min(int(b), int(d)) <= max(int(b), int(d)):
            print('hit3')
            final_value += 1
    elif int(a) == int(c):
        if min(int(b), int(d)) <= max(int(b), int(d)):
            print('hit4')
            final_value += 1


print(final_value)