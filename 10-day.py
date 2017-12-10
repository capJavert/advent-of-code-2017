import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/RFnduz1C")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    lengths = [ord(i) for i in get_and_prepare_data_string()] + [17, 31, 73, 47, 23]

    a = [i for i in range(256)]
    p, skip = 0, 0

    for i in range(64):
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

    dense_hash = []
    xors = ["^".join([str(i) for i in a[i*16:(i+1)*16]]) for i in range(16)]

    for xor in xors:
        exec('dense_hash.append(hex('+xor+')[2:].zfill(2))')

    print("".join(dense_hash))


main()
