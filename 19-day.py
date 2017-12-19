import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/Eg7eq2Sd")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    maze = get_and_prepare_data_string().splitlines()

    letters = [str(chr(i)) for i in range(65, 91)]
    collected = []
    direction = "D"
    steps = 0

    p = [0, maze[0].index("|")]

    while True:
        character = maze[p[0]][p[1]]

        if character == "+":
            turned = False

            if p[0]-1 >= 0 and not turned:
                if maze[p[0]-1][p[1]] != " " and direction != "D":
                    direction = "U"
                    turned = True

            if p[1]+1 < len(maze[p[0]]) and not turned:
                if maze[p[0]][p[1]+1] != " " and direction != "L":
                    direction = "R"
                    turned = True

            if p[0]+1 < len(maze) and not turned:
                if maze[p[0]+1][p[1]] != " " and direction != "U":
                    direction = "D"
                    turned = True

            if p[1]-1 >= 0 and not turned:
                if maze[p[0]][p[1]-1] != " " and direction != "R":
                    direction = "L"

        if character != " ":
            steps += 1

            if character in letters:
                collected.append(character)

            if direction == "U":
                p = (p[0]-1, p[1])

            if direction == "R":
                p = (p[0], p[1]+1)

            if direction == "D":
                p = (p[0]+1, p[1])

            if direction == "L":
                p = (p[0], p[1]-1)
        elif character == " ":
            break

    print("".join(collected), steps)


main()
