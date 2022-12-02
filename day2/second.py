with open("input.txt") as file:
    lines = file.read().splitlines()
    result = 0
    match_play = {
        # Lose
        'X': {
            'A': 3,
            'B': 1,
            'C': 2
        },
        # Draw
        'Y': {
            'A': 1,
            'B': 2,
            'C': 3
        },
        # win
        'Z': {
            'A': 2,
            'B': 3,
            'C': 1
        }
    }
    for line in lines:
        print(line)
        opponent = line[0]
        ending = line[-1]
        r = match_play.get(ending).get(opponent)
        print("match", r)
        result += r

        match ending:
            case 'Y':
                print("draw")
                result += 3
            case 'Z':
                print("win")
                result += 6
            case 'X':
                print("lose")
                pass
        print("Result", result)
    print(result)
