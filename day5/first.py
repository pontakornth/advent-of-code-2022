with open("real_input.txt") as file:
    content = file.read()
    first_half, second_half = content.split("---")
    # 1 A B C D
    stack = dict()
    for line in first_half.splitlines():
        key, *value = line.split()
        stack[key] = value
    print(stack)
    # move N from S to D
    for line in second_half.strip().splitlines():
        input_line = line.split()
        times = int(input_line[1])
        source = input_line[3]
        destination = input_line[-1]
        for i in range(times):
            stack.get(destination).append(stack.get(source).pop())
    for key, value in stack.items():
        print(key, value)
