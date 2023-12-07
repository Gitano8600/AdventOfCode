from collections import Counter

file = open("input.txt", "r")
values = file.read().splitlines()
hand_list = []
result_value = 0

mapping_dict = {
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "T": "J",
    "J": "A",
    "Q": "K",
    "K": "L",
    "A": "M"
}

for value in values:
    hand_value = "".join(sorted([str(x) for x in Counter(value[:5]).values()],
                                reverse=True))[:2].ljust(2, "0")
    hand_value_j = ""
    if "J" in value[:5]:
        print("has J", "hand_value", hand_value)
        ctr = Counter(value[:5])["J"]
        if hand_value == "41":
            hand_value = "50" if ctr in [1, 4] else hand_value
        elif hand_value == "32":
            hand_value = "50" if ctr in [2, 3] else hand_value
        elif hand_value == "31":
            hand_value = "41" if ctr in [1, 3] else hand_value
        elif hand_value == "22":
            if ctr == 1:
                hand_value = "32"
            elif ctr == 2:
                hand_value = "41"
        elif hand_value == "21":
            hand_value = "31" if ctr in [1, 2] else hand_value
        elif hand_value == "11":
            hand_value = "21"

    hand_rank = "".join([mapping_dict[x] for x in value[:5]])
    hand_list.append((value[:5], int(value[5:].strip()), hand_value + hand_rank))

for idx, val in enumerate(sorted(hand_list, key=lambda x: x[2])):
    result_value += (idx+1) * val[1]

print(result_value)
