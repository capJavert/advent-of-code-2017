import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/M1U71PJX")
    # request = requests.get("https://pastebin.com/raw/RKjqkZem")
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

    for x in range(10000):
        if grid[str(p)] == "#":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

        if str(p) in grid:
            if grid[str(p)] == "#":
                grid[str(p)] = "."
            else:
                grid[str(p)] = "#"
                infections += 1
        else:
            grid[str(p)] = "#"
            infections += 1

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
