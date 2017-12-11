import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/zM66MGma")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    directions = get_and_prepare_data_string().split(",")

    x, y, z = 0, 0, 0
    breadcrumbs = []

    for direction in directions:
        if "n" == direction:
            y += 1
            z -= 1

        if "ne" == direction:
            z -= 1
            x += 1

        if "nw" == direction:
            y += 1
            x -= 1

        if "s" == direction:
            y -= 1
            z += 1

        if "se" == direction:
            y -= 1
            x += 1

        if "sw" == direction:
            x -= 1
            z += 1

        breadcrumbs.append((abs(x) + abs(y) + abs(z)) / 2)

    print(breadcrumbs[-1], max(breadcrumbs))


main()
