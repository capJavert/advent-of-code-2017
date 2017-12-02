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
        max_value = 0
        min_value = 10000

        for digit in line.split("\t"):
            digit = int(digit)

            if digit < min_value:
                min_value = digit

            if digit > max_value:
                max_value = digit

        checksum += max_value - min_value

    print(checksum)


main()
