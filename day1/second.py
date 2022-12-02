with open("input.txt") as file:
    content = file.read()
    lines = content.splitlines()
    lines.append('')
    print(lines)
    current = 0
    result = []
    for line in lines:
        if not line.isdigit():
            result.append(current)
            current = 0
        else:
            n_line = int(line)
            current += n_line
    print(sum(sorted(result, reverse=True)[:3]))
