import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/qw92d5iX")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    sequence = get_and_prepare_data_string().split(",")
    # sequence = ["s1", "x3/4", "pe/b"]
    programs = [chr(i) for i in range(97, 113)]
    # programs = [chr(i) for i in range(97, 102)]

    for dance_move in sequence:
        if dance_move.startswith("s"):
            programs = programs[-int(dance_move[1:]):] + programs[:-int(dance_move[1:])]

        if dance_move.startswith("x"):
            p1, p2 = dance_move[1:].split("/")
            s = programs[int(p2)]
            programs[int(p2)] = programs[int(p1)]
            programs[int(p1)] = s

        if dance_move.startswith("p"):
            p1, p2 = dance_move[1:].split("/")
            p1, p2 = programs.index(p1), programs.index(p2)
            s = programs[int(p2)]
            programs[int(p2)] = programs[int(p1)]
            programs[int(p1)] = s

    print("".join(programs))


main()
