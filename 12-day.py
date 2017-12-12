import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/J9afAYZW")
    request.encoding = 'ISO-8859-1'

    return request.text


def into_the_pipe(current, previous):
    global root_count

    previous.append(current)
    root_count += 1

    for pipe in pipes[current]:
        if pipe in previous:
            continue

        into_the_pipe(pipe, previous)


root_count = 0
pipes = {}


def main():
    data = get_and_prepare_data_string().splitlines()

    for pipe in data:
        pipes[pipe.split(" <-> ")[0]] = pipe.split(" <-> ")[1].split(", ")

    into_the_pipe("0", [])

    print(root_count)


main()
