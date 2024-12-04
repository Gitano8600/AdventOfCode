file = open("input.txt", "r")
values = file.read()


class Letterjumble:

    def __init__(self, jumblestring, pattern, bullseye_pattern='SAM'):
        self.jumblestring = jumblestring.splitlines()
        self.pattern = pattern
        self.bullseye_pattern = bullseye_pattern
        self.bullseye = bullseye_pattern[len(bullseye_pattern)//2]
        self.pattern_occurences = 0
        self.xmas_pattern_occurences = 0

        self.len_col = len(self.jumblestring[0])
        self.len_row = len(self.jumblestring)
        self.js_horizontal = ['' for _ in range(self.len_row)]
        self.js_vertical = ['' for _ in range(self.len_col)]
        self.js_diag_horizontal = ['' for _ in range(self.len_row + self.len_col -1)]
        self.js_diag_vertical = ['' for _ in range(len(self.js_diag_horizontal))]
        self.min_diag_vertical = -self.len_row + 1

        self.directions = [
            self.js_horizontal,
            self.js_vertical,
            self.js_diag_horizontal,
            self.js_diag_vertical
        ]

        self.fill()


    def fill(self):
        for x in range(self.len_col):
            for y in range(self.len_row):
                self.js_horizontal[y] += self.jumblestring[y][x]
                self.js_vertical[x] += self.jumblestring[y][x]
                self.js_diag_horizontal[x+y] += self.jumblestring[y][x]
                self.js_diag_vertical[x-y-self.min_diag_vertical] += self.jumblestring[y][x]


    def count_patterns(self):
        for direction in self.directions:
            for line in direction:
                self.pattern_occurences += line.count(self.pattern)
                self.pattern_occurences += line[::-1].count(self.pattern)

        return self.pattern_occurences


    def count_xmas_patterns(self):
        for index, line in enumerate(self.js_horizontal):

            if index == 0 or index == len(self.js_horizontal)-1:
                continue

            bullseye_position = [pos for pos, char in enumerate(line) if char == self.bullseye]


            for pos in bullseye_position:

                if pos == 0 or pos == len(line)-1:
                    continue

                if self.js_horizontal[index-1][pos-1] == self.js_horizontal[index+1][pos+1] :
                    #to avoid SAS/MAM cases
                    continue

                if self.js_horizontal[index-1][pos+1] == self.js_horizontal[index+1][pos-1] :
                    # to avoid SAS/MAM cases
                    continue


                surroundings = ''.join(sorted(
                    self.js_horizontal[index-1][pos-1]+
                    self.js_horizontal[index-1][pos+1]+
                    self.js_horizontal[index+1][pos-1]+
                    self.js_horizontal[index+1][pos+1]))


                if surroundings == 'MMSS':
                    self.xmas_pattern_occurences += 1

        return self.xmas_pattern_occurences



day4_jumble = Letterjumble(values, 'XMAS', 'SAM')
print(day4_jumble.count_xmas_patterns())
