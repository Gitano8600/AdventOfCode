file = open("input.txt", "r")
values = file.read().splitlines()
final_score = 0


def get_outcome(elf, outcome):
    constellations = {
        'A': dict(X=3, Y=1, Z=2),
        'B': dict(X=1, Y=2, Z=3),
        'C': dict(X=2, Y=3, Z=1)
                 }

    hand_values = dict(X=0, Y=3, Z=6)

    return constellations[elf][outcome] + hand_values[outcome]


for value in values:
    final_score += get_outcome(value[0], value[2])

print(final_score)
