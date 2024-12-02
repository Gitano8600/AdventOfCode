file = open("input.txt", "r")
values = file.read().splitlines()
result = 0


def conditions_met(listofnumbers):
    listofintegers = list(map(int, listofnumbers.split()))
    graduality = (sorted(listofintegers) == listofintegers) or (sorted(listofintegers, reverse=True) == listofintegers)

    if not graduality:
        return False

    for index, number in enumerate(listofintegers[1:]):
        if not 0 < abs(listofintegers[index] - listofintegers[index+1]) < 4:
            return False

    return True


for value in values:
    if conditions_met(value):
        result += 1

print(result)
