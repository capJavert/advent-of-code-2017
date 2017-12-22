import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/M1U71PJX")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    grid = {}
    data = get_and_prepare_data_string().splitlines()
    p = [int(len(data)/2), (len(data[0])/2)]

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            grid[str([i, j])] = c

    directions = ["L", "U", "R", "D"]
    d = 1
    infections = 0

    for x in range(10000000):
        if grid[str(p)] == "#":
            d = (d + 1) % 4
        elif grid[str(p)] == "F":
            d = (d + 2) % 4
        elif grid[str(p)] == ".":
            d = (d - 1) % 4

        if grid[str(p)] == ".":
            grid[str(p)] = "W"
        elif grid[str(p)] == "W":
            grid[str(p)] = "#"
            infections += 1
        elif grid[str(p)] == "#":
            grid[str(p)] = "F"
        elif grid[str(p)] == "F":
            grid[str(p)] = "."

        if directions[d] == "U":
            p[0] -= 1

        if directions[d] == "R":
            p[1] += 1

        if directions[d] == "D":
            p[0] += 1

        if directions[d] == "L":
            p[1] -= 1

        if str(p) not in grid:
            grid[str(p)] = "."

    print(infections)


main()
