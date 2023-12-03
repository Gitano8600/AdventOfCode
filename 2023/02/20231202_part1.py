file = open("input.txt", "r")

values = file.read().splitlines()

final_sum = 0
final_sum_exp_test = 8
limit_red = 12
limit_green = 13
limit_blue = 14

for item in values:
    is_candidate = True
    game_nr = item.split(":")[0].lstrip("Game ")
    game_info = item.split(":")[1].split(";")

    for game in game_info:
        for rnd in game.split(","):
            if ("red" in rnd) and (int(rnd.split()[0]) > limit_red):
                is_candidate = False

            elif ("green" in rnd) and (int(rnd.split()[0]) > limit_green):
                is_candidate = False

            elif ("blue" in rnd) and (int(rnd.split()[0]) > limit_blue):
                is_candidate = False

    if is_candidate:
        final_sum += int(game_nr)

print(final_sum)

