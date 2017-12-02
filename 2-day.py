import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/CCCrdQG2")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    spreadsheet = get_and_prepare_data_string()

    checksum = 0

    for line in spreadsheet.splitlines():
        for digit1 in line.split("\t"):
            digit1 = int(digit1)

            for digit2 in line.split("\t"):
                digit2 = int(digit2)

                if digit1 != digit2:
                    if digit1 % digit2 == 0:
                        checksum += digit1 / digit2
                        break

    print(int(checksum))


main()
