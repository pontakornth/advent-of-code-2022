import re
result = 0
with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        l = list(line)
        first_half, second_half = l[:len(l)//2], l[len(l)//2:]
        priority_char = list(set(first_half).intersection(set(second_half)))[0]
        if re.match(r'^[a-z]$', priority_char):
            result += ord(priority_char) - 96  # 1 is the first value
        else:
            result += ord(priority_char) - 65 + 27
    print(result)
