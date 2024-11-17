import re

file = open("input.txt", "r")
values = file.read().splitlines()
final_score = 0

print(values)

def grouper(all_groups, group_size=3):
    for item in range(0, len(all_groups), group_size):
        yield all_groups[item:item + group_size]


def find_common_char(pattern):
    pattern1, pattern2, pattern3 = pattern
    regex = re.compile(f"[{re.escape(pattern2)}]")
    return [char for char in pattern1 if regex.match(char) and char in pattern3][0]


def return_prio(item):
    if item.islower():
        return ord(item) - ord('a')+1
    else:
        return ord(item) - ord('A')+27


for value in grouper(values):
    print(value)
    final_score += return_prio(find_common_char(value))

print(final_score)
