import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/5Tgh4PAA")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    digit_sequence = get_and_prepare_data_string()

    sum_count = 0

    for (i, character) in enumerate(digit_sequence):
        if i == len(digit_sequence)-1:
            next_character = digit_sequence[0]
        else:
            next_character = digit_sequence[i+1]

        if character == next_character:
            sum_count += int(next_character)

    print(sum_count)


main()
