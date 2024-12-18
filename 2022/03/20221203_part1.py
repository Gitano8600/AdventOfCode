import re

file = open("input.txt", "r")
values = file.read().splitlines()
final_score = 0


def find_common_char(pattern):
    pattern1, pattern2 = pattern[:len(pattern)//2], pattern[len(pattern)//2:]
    regex = re.compile(f"[{re.escape(pattern2)}]")
    return [char for char in pattern1 if regex.match(char)][0]


def return_prio(item):
    if item.islower():
        return ord(item) - ord('a')+1
    else:
        return ord(item) - ord('A')+27


for value in values:
    final_score += return_prio(find_common_char(value))

print(final_score)
