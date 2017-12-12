import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/J9afAYZW")
    request.encoding = 'ISO-8859-1'

    return request.text


def into_the_pipe(current, previous):
    previous.append(current)

    for pipe in pipes[current]:
        if pipe in previous:
            continue

        previous = into_the_pipe(pipe, previous)

    return previous


pipes = {}
groups = []


def main():
    data = get_and_prepare_data_string().splitlines()

    for pipe in data:
        pipes[pipe.split(" <-> ")[0]] = pipe.split(" <-> ")[1].split(", ")

    for pipe in pipes:
        group = set(into_the_pipe(pipe, []))
        if group not in groups:
            groups.append(set(group))

    print(len(groups))


main()
