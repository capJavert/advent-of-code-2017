import requests
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/zM66MGma")
    request.encoding = 'ISO-8859-1'

    return request.text


def cord_to_hex(x, y):
    breadcrumbs[y][x] = 0
    breadcrumbs[y+1][x] = 0
    breadcrumbs[y-1][x] = 0
    breadcrumbs[y][x+1] = 0
    breadcrumbs[y][x-1] = 0
    breadcrumbs[y+1][x+1] = 0
    breadcrumbs[y-1][x-1] = 0

    breadcrumbs[y+1][x-1] = 1
    breadcrumbs[y-1][x+1] = 1


size = 3100  # this is the lowest approx number that was enough for breadcrumbs path TODO: optimize for step 2
breadcrumbs = [[0 for _ in range(size)] for _ in range(size)]


def main():
    directions = get_and_prepare_data_string().split(",")

    x, y = int(size/2), int(size/2)
    start = (x, y)

    cord_to_hex(x, y)

    for direction in directions:
        if "n" == direction:
            x -= 1
            y -= 1

        if "ne" == direction:
            y -= 1

        if "nw" == direction:
            x -= 1

        if "s" == direction:
            x += 1
            y += 1

        if "se" == direction:
            x += 1

        if "sw" == direction:
            y += 1

        cord_to_hex(x, y)

    target = (x, y)

    grid = Grid(matrix=breadcrumbs)

    start = grid.node(start[0], start[1])
    end = grid.node(target[0], target[1])

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    print(len(path)-1)


main()
