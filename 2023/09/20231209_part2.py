file = open("input.txt", "r")
values = file.read().splitlines()
final_value = 0

list_of_histories = []
list_all_seq = [[*map(int, line.split())] for line in values]


for seq in list_all_seq:
    list_cur_seq = [seq[::-1]]
    zero_reached = True

    while zero_reached:
        next_list = [x[0] - x[1] for x in zip(list_cur_seq[-1][1:], list_cur_seq[-1])]
        print(next_list)
        list_cur_seq.append(next_list)
        zero_reached = any(next_list)

    list_of_histories.append(list_cur_seq)


for history in list_of_histories:
    history_value = 0

    for i in reversed(range(len(history))):
        history_value += history[i-1][-1]

    final_value += history_value

print(final_value)
