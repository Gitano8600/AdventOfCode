file = open("input.txt", "r")
values = file.read().splitlines()
result = 0


def conditions_met(listofintegers):
    graduality = (sorted(listofintegers) == listofintegers) or (sorted(listofintegers, reverse=True) == listofintegers)

    if not graduality:
        return False

    for index, number in enumerate(listofintegers[1:]):
        if not 0 < abs(listofintegers[index] - listofintegers[index+1]) < 4:
            return False

    return True


for value in values:
    listofnumbers = list(map(int, value.split()))
    if conditions_met(listofnumbers):
        result += 1
        continue
    else:
        for variation in range(len(listofnumbers)):
            listvariation = listofnumbers.copy()
            listvariation.pop(variation)
            if conditions_met(listvariation):
                result += 1
                break


print(result)
