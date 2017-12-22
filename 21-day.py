import numpy as np
import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/MEn2WvCD")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    artists_book_of_enhancement = [line.strip().split(" => ") for line in get_and_prepare_data_string().splitlines()]

    art = [
        [".", "#", "."],
        [".", ".", "#"],
        ["#", "#", "#"]
    ]

    art = np.array(art)
    script_of_enhancement = {}

    for rule in artists_book_of_enhancement:
        pattern = [list(i.encode('utf8')) for i in rule[0].split("/")]
        enhancement = [list(i.encode('utf8')) for i in rule[1].split("/")]

        for i in range(8):
            if i == 4:
                pattern = np.flipud(pattern)

            pattern = np.rot90(pattern, i)

            script_of_enhancement[str(pattern)] = enhancement

    for x in range(18):
        if len(art) % 2 == 0:
            n = np.array([])

            for b in range(len(art), step=2):
                rows = []

                for b2 in range(len(art), step=2):
                    block = art[b:b+2, b2:b2+2]

                    rule = script_of_enhancement[str(block)]

                    rows.append(rule)

                if len(n) == 0:
                    n = np.hstack(tuple(rows))
                else:
                    n = np.vstack((n, np.hstack(tuple(rows))))
        else:
            n = np.array([])

            for b in range(len(art), step=3):
                rows = []
                for b2 in range(len(art), step=3):
                    block = art[b:b+3, b2:b2+3]

                    rule = script_of_enhancement[str(block)]

                    if int(len(art) / 3) == 1:
                        rows += rule
                    else:
                        rows.append(rule)

                if int(len(art) / 3) == 1:
                    n = np.array(rows)
                else:
                    if len(n) == 0:
                        n = np.hstack(tuple(rows))
                    else:
                        n = np.vstack((n, np.hstack(tuple(rows))))

        art = n.copy()
        print(x, len(art), len(art[0]))

    unique, counts = np.unique(art, return_counts=True)
    print(dict(zip(unique, counts))["#"])


main()
