with open("input.txt") as file:
    lines = file.read().splitlines()
    result = 0
    loss = ['A Z', 'B X', 'C Y']
    win = ['A Y', 'B Z', 'C X']
    for line in lines:
        if line in loss:
            pass
        elif line in win:
            result += 6
        else:
            result += 3
        shape = line[-1]
        match shape:
            case 'X':
                result += 1
            case 'Y':
                result += 2
            case 'Z':
                result += 3
    print(result)
