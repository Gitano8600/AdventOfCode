file = open("input.txt", "r")
values = file.read().splitlines()
final_value = 0

list_of_histories = []

for line in values:
    tuple_of_seq = ((tuple(int(i) for i in line.split(" ")),))
    zero_reached = True

    while zero_reached:
        next_tuple = tuple([x[0] - x[1] for x in zip(tuple_of_seq[-1][1:], tuple_of_seq[-1])])
        tuple_of_seq = (tuple_of_seq) + (next_tuple,)
        zero_reached = any(next_tuple)

    list_of_histories.append(tuple_of_seq)

for history in list_of_histories:
    history_value = 0
    for i in reversed(range(len(history))):
        history_value += history[i-1][-1]
    final_value += history_value

print(final_value)
