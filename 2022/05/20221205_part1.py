import re

file = open("input.txt", "r")
raw_stacks, raw_moves = file.read().split("\n\n")
solution_string = ''


def create_stacks_list(raw_stacks):
    unf_stacks = raw_stacks.split("\n")
    unf_stacks.reverse()
    first_row = unf_stacks.pop(0)
    n_stacks = len(first_row.split())

    stacks_list = [[] for i in range(n_stacks)]

    for line in unf_stacks:
        index = 0
        for position in range(1, len(line), 4):
            if line[position] != " ":
                stacks_list[index].append(line[position])
            index += 1

    return stacks_list


def get_moves(raw_moves):
    unf_moves = raw_moves.split("\n")[:-1]
    print('unf_moves', unf_moves)
    moves_list = []
    for move_pattern in unf_moves:
        moves_list.append([int(i) for i in re.findall(r"[\d']+", move_pattern)])

    return moves_list


stacks = create_stacks_list(raw_stacks)
moves = get_moves(raw_moves)


for move in moves:
    for i in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1]-1][-1])
        stacks[move[1]-1].pop()


for stack in stacks:
    solution_string += stack[-1]

print(solution_string)


