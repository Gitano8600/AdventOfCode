import re

regex = re.compile('[+@_!#=$%^&*()<>?/|}{~:-]')

file = open("input.txt", "r")
values = file.read().splitlines()
final_sum = 0


def find_char_pos(pattern, string, position="start"):
    positions = []
    for mtch in re.finditer(pattern, string):
        if position == "start":
            positions.append(mtch.start())
        elif position == "end":
            positions.append(mtch.end())
    return positions


for idx, item in enumerate(values):

    special_char_pos_cur_line = find_char_pos(regex, values[idx])

    for nbr in re.finditer(r"[0-9]+", item):
        nbr_qualifier = False

        start = nbr.start()
        end = nbr.end()

        # check current line
        for match in special_char_pos_cur_line:
            if (match+1 == start) or (match == end):
                nbr_qualifier = True

        # check next line
        if idx != (len(values) - 1):
            special_char_pos_next_line = find_char_pos(regex, values[idx + 1])
            for match in special_char_pos_next_line:
                if (match - 1 in [start]) or (match+1 in [start, end]) or (match in [start, end]):
                    nbr_qualifier = True

        # check previous line
        if idx != 0:
            special_char_pos_next_line = find_char_pos(regex, values[idx - 1])
            for match in special_char_pos_next_line:
                if (match - 1 in [start]) or (match+1 in [start, end]) or (match in [start, end]):
                    nbr_qualifier = True

        if nbr_qualifier:
            final_sum += int(nbr.group())

print(final_sum)



