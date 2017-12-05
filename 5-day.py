import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/n37ZVwjj")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    instructions = get_and_prepare_data_string().splitlines()

    steps = 0
    index = 0

    while index < len(instructions):
        jump = int(instructions[index])

        if jump >= 3:
            instructions[index] = jump - 1
        else:
            instructions[index] = jump + 1

        index += jump

        steps += 1

    print(steps)


main()
