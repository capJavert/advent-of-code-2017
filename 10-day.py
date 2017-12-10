import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/RFnduz1C")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    lengths = get_and_prepare_data_string().split(",")

    a = [i for i in range(256)]
    p, skip = 0, 0

    for length in lengths:
        length = int(length)

        if length <= 1:
            pass
        else:
            sub = (a[p:p + length]+a[:length - len(a[p:p + length])])[::-1]
            a[p:p + length] = sub[:len(a[p:p + length])]
            a[:length - len(a[p:p + length])] = sub[len(a[p:p + length]):]

        p = (p + (length+skip)) % len(a)
        skip += 1

    print(a[0]*a[1])


main()
