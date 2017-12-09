import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/a83ELw6K")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    data = get_and_prepare_data_string()

    score = 0
    ignore = False
    garbage = False
    groups = []

    for i, c in enumerate(data):
        if ignore:
            ignore = False
            continue

        if c == "!" and garbage:
            ignore = True
            continue

        if c == "<":
            garbage = True

        if c == ">":
            garbage = False

        if c == "{" and not garbage:
            groups.append(len(groups)+1)

        if c == "}" and not garbage:
            score += groups[-1]
            groups.pop()

    print(score)


main()
