with open("input.txt") as file:
    content = file.read()
    char_set = set()
    char_count = 0
    for i in range(len(content) - 4):
        char_count += 1
        chars = content[i:i+4]
        if len(chars) == len(set(chars)):
            print(char_count + 3)
            break
