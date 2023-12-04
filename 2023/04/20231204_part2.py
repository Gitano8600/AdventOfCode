file = open("input.txt", "r")
values = file.read().splitlines()
final_sum = 0
dict_of_cards = dict()

for i in values:
    count = 0
    card_id = int(i.split(":")[0].lstrip("Card "))
    winning_numbers = i.split(":")[1].split("|")[0].strip().split()
    card_numbers = i.split(":")[1].split("|")[1].strip().split()

    for nbr in winning_numbers:
        if nbr in card_numbers:
            count += 1

    dict_of_cards[card_id] = {"wins": count,
                              "instances": 1}

for key, value in dict_of_cards.items():
    if value['wins'] != 0:
        for occ in range(value['instances']):
            counter = key
            for win in range(value['wins']):
                counter += 1
                dict_of_cards[counter]['instances'] += 1

for value in dict_of_cards.values():
    final_sum += value['instances']

print(final_sum)
