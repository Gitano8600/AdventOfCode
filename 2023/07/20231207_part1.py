from collections import Counter

file = open("input.txt", "r")
values = file.read().splitlines()
hand_list = []
result_value = 0

mapping_dict = {
    "2": "A",
    "3": "B",
    "4": "C",
    "5": "D",
    "6": "E",
    "7": "F",
    "8": "G",
    "9": "H",
    "T": "I",
    "J": "J",
    "Q": "K",
    "K": "L",
    "A": "M"
}

for value in values:
    hand_value = "".join(sorted([str(x) for x in Counter(value[:5]).values()],
                                reverse=True)).ljust(0, "0")
    hand_rank = "".join([mapping_dict[x] for x in value[:5]])
    hand_list.append((value[:5], int(value[5:].strip()), hand_value + hand_rank))

for idx, val in enumerate(sorted(hand_list, key=lambda x: x[2])):
    result_value += (idx+1) * val[1]

print(result_value)
