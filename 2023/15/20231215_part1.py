file = open("input.txt", "r")
values = file.read()
final_value = 0


def hash_string(hash_str, n=0):
    new_value = (ord(hash_str[0])+n) * 17 % 256
    if len(hash_str) == 1:
        return new_value
    else:
        return hash_string(hash_str[1:], new_value)


for value in values.split(","):
    final_value += hash_string(value)

print(final_value)
