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

    ignore = False
    garbage = False
    garbage_counter = 0

    for i, c in enumerate(data):
        if ignore:
            ignore = False
            continue

        if c == "!" and garbage:
            ignore = True
            continue

        if c == "<" and not garbage:
            garbage = True
            continue

        if c == ">":
            garbage = False
            continue

        if c == "{" and not garbage:
            continue

        if c == "}" and not garbage:
            continue

        if garbage:
            garbage_counter += 1

    print(garbage_counter)


main()
