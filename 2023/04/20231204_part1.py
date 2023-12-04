file = open("input.txt", "r")
values = file.read().splitlines()
final_sum = 0

values_without_card = [i.split(":")[1] for i in values]

for i in values_without_card:
    count = 0
    winning_numbers = (i.split("|")[0].strip()).split()
    card_numbers = (i.split("|")[1].strip()).split()

    for nbr in winning_numbers:
        if nbr in card_numbers:
            count = count * 2 if count != 0 else 1
    final_sum += count

print(final_sum)
