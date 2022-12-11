import re
result = 0
with open("input.txt") as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        priority_char = [c for c in set.intersection(
            *(set(line) for line in group))][0]
        if re.match(r'^[a-z]$', priority_char):
            result += ord(priority_char) - 96  # 1 is the first value
        else:
            result += ord(priority_char) - 65 + 27
    print(result)
