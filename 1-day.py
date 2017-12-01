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

    halfway_step = int(len(digit_sequence)/2)
    sum_count = 0

    for (i, character) in enumerate(digit_sequence):
        next_character = digit_sequence[(i+halfway_step) % len(digit_sequence)]

        if character == next_character:
            sum_count += int(next_character)

    print(sum_count)


main()
