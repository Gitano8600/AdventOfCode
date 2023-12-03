
file = open("input.txt", "r")

values = file.read().splitlines()

final_sum = 0
final_sum_exp_test = 8
limit_red = 12
limit_green = 13
limit_blue = 14

for item in values:

    game_nr = item.split(":")[0].lstrip("Game ")
    game_info = item.split(":")[1].split(";")
    max_red = 0
    max_green = 0
    max_blue = 0

    for game in game_info:
        for rnd in game.split(","):

            if ("red" in rnd) and (int(rnd.split()[0]) > max_red):
                max_red = int(rnd.split()[0])

            elif ("green" in rnd) and (int(rnd.split()[0]) > max_green):
                max_green = int(rnd.split()[0])

            elif ("blue" in rnd) and (int(rnd.split()[0]) > max_blue):
                max_blue = int(rnd.split()[0])

    final_sum += max_red * max_green * max_blue

print(final_sum)
