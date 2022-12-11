def is_covered(a, b, c, d):
    """
    If range a - b and c - d, cover one another, returns True. Otherwise, return False.

    Assume a <= b and c <= d.
    """
    if a <= c and d <= b:
        return True
    elif c <= a and b <= d:
        return True
    else:
        return False


count = 0
with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        ab, cd = line.split(",")
        a, b = [int(x) for x in ab.split("-")]
        c, d = [int(x) for x in cd.split("-")]
        if is_covered(a, b, c, d):
            print(f"({a}, {b}) overlapped ({c}, {d})")
            count += 1
    print(count)
