file = open("input.txt", "r")
values = file.read().splitlines()
final_value = 0


def longer_range(pattern):
    range1, range2 = pattern.split(',')
    range1_length = int(range1.split('-')[1]) - int(range1.split('-')[0])
    range2_length = int(range2.split('-')[1]) - int(range2.split('-')[0])
    if range1_length > range2_length:
        return 'first'
    elif range2_length > range1_length:
        return 'second'
    elif (range2_length == range1_length) and (range1 == range2):
        return 'even'
    else:
        return 'other'


def is_within(long_pattern, short_pattern):
    if int(long_pattern.split('-')[1]) >= int(short_pattern.split('-')[1]):
        if int(long_pattern.split('-')[0]) <= int(short_pattern.split('-')[0]):
            return True
    return False


for value in values:
    longer_pattern = longer_range(value)
    if longer_pattern == 'first':
        if is_within(value.split(',')[0], value.split(',')[1]):
            final_value += 1
    elif longer_pattern == 'second':
        if is_within(value.split(',')[1], value.split(',')[0]):
            final_value += 1
    elif longer_pattern == 'even':
        final_value += 1


print(final_value)
