from heapq import heappop, heappush


def knot_hash(data):
    lengths = [ord(i) for i in data] + [17, 31, 73, 47, 23]

    a = [i for i in range(256)]
    p, skip = 0, 0

    for i in range(64):
        for length in lengths:
            length = int(length)

            if length <= 1:
                pass
            else:
                sub = (a[p:p + length] + a[:length - len(a[p:p + length])])[::-1]
                a[p:p + length] = sub[:len(a[p:p + length])]
                a[:length - len(a[p:p + length])] = sub[len(a[p:p + length]):]

            p = (p + (length + skip)) % len(a)
            skip += 1

    dense_hash = []
    xors = ["^".join([str(i) for i in a[i * 16:(i + 1) * 16]]) for i in range(16)]

    for xor in xors:
        exec('dense_hash.append(hex(' + xor + ')[2:].zfill(2))')

    return "".join(dense_hash)


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def find_path_astar(maze, start):
    goal = (len(maze) - 1, len(maze[0]) - 1)
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    visited = set()
    graph = maze2graph(maze)

    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return visited
        if current in visited:
            continue
        visited.add(current)
        # print(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (cost + heuristic(neighbour, goal), cost + 1,
                                path + direction, neighbour))
    return visited


def main():
    puzzle_input = "oundnydw"

    grid = []
    groups = []

    for i in range(128):
        grid.append(
            list("".join(format(int(c, 16), '04b') for c in knot_hash("".join([puzzle_input, "-", str(i)])))
                 .replace("1", "X").replace("0", "1").replace("X", "0"))
        )
    grid = [[int(square) for square in block] for block in grid]

    for i, block in enumerate(grid):
        for j, square in enumerate(block):
            if any((i, j) in group for group in groups) or square == 1:
                continue

            groups.append(find_path_astar(grid, (i, j)))

    print(len(groups))


main()
