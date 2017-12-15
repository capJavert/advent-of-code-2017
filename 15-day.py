
def gen_a(value):
    return (value*16807) % 2147483647


def gen_b(value):
    return (value*48271) % 2147483647


def main():
    a, b = 699, 124

    final_countdown = 0

    for i in range(40000000):
        a = gen_a(a)
        b = gen_b(b)

        if "".join(format(a, '032b'))[16:] == "".join(format(b, '032b'))[16:]:
            final_countdown += 1

    print(final_countdown)


main()
