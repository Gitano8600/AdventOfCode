file = open("input.txt", "r")
values = file.read().splitlines()
final_score = 0


def get_outcome(elf, me):
    hand_map = { 'A': 1,
                 'B': 2,
                 'C': 3,
                 'X': 1,
                 'Y': 2,
                 'Z': 3}
    int_elf = hand_map[elf]
    int_me = hand_map[me]

    if int_elf == int_me:
        return 3 + int_me
    elif int_elf - int_me in [-1, 2]:
        return 6 + int_me
    else:
        return int_me


for value in values:
    final_score += get_outcome(value[0], value[2])

print(final_score)
