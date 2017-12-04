import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/npLGrLhA")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    passphrases = get_and_prepare_data_string()
    valid_passphrases = 0

    for line in passphrases.splitlines():
        is_valid = True
        words = []

        for word in line.split(" "):
            if word in words:
                is_valid = False
                break

            words.append(word)

        if is_valid:
            valid_passphrases += 1

    print(valid_passphrases)


main()
