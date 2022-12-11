def is_overlapped(a, b, c, d):
    """
    If range a - b and c - d, overlap one another, returns True. Otherwise, return False.

    Assume a <= b and c <= d.
    """
    # It is the most readable way I found.
    return a <= d and c <= b


count = 0
with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        ab, cd = line.split(",")
        a, b = [int(x) for x in ab.split("-")]
        c, d = [int(x) for x in cd.split("-")]
        if is_overlapped(a, b, c, d):
            print(f"({a}, {b}) overlapped ({c}, {d})")
            count += 1
    print(count)
