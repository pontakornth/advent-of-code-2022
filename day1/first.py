with open("input.txt") as file:
    content = file.read()
    lines = content.splitlines()
    lines.append('')
    print(lines)
    current, max_cal = 0, 0
    for line in lines:
        if not line.isdigit():
            if current > max_cal:
                max_cal = current
            current = 0
        else:
            n_line = int(line)
            current += n_line
    print(max_cal)
