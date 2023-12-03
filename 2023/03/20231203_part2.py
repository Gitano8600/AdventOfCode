import re
import math

regex = re.compile('[*]')
regex_general = re.compile('[+@_!#=$%^&()<>?/|}{~:-]')

file = open("input.txt", "r")
values = file.read().splitlines()

final_sum = 0


def find_char_pos(pattern, string, position="start"):
    positions = []
    for match in re.finditer(pattern, string):
        if position == 'start':
            positions.append(match.start())
        elif position == 'end':
            positions.append(match.end())
    return positions


for idx, item in enumerate(values):
    if not find_char_pos(regex, values[idx]):
        continue

    special_char_pos_cur_line = find_char_pos(regex, values[idx])

    for char_pos in special_char_pos_cur_line:
        selected_numbers = []
        numbers_prev = re.finditer(r"[0-9]+", values[idx - 1]) if idx != 0 else None
        numbers_curr = re.finditer(r"[0-9]+", values[idx])
        numbers_next = re.finditer(r"[0-9]+", values[idx + 1]) if idx != (len(values) - 1) else None

        for nbr in numbers_prev:
            if (char_pos - 1 == nbr.start()) or (char_pos +1 in [nbr.start(), nbr.end()]) or char_pos in [nbr.start(), nbr.end()]:
                selected_numbers.append(int(nbr.group()))

        for nbr in numbers_curr:
            if (char_pos + 1 == nbr.start()) or (char_pos == nbr.end()):
                selected_numbers.append(int(nbr.group()))

        for nbr in numbers_next:
            if (char_pos - 1 == nbr.start()) or (char_pos + 1 in [nbr.start(), nbr.end()]) or char_pos in [nbr.start(), nbr.end()]:
                selected_numbers.append(int(nbr.group()))

        if len(selected_numbers) >= 2:
            final_sum += math.prod(selected_numbers)

print(final_sum)







