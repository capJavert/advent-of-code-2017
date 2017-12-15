
def gen_a(value):
    next_value = (value * 16807) % 2147483647

    while next_value % 4 != 0:
        value = next_value
        next_value = (value*16807) % 2147483647

    return next_value


def gen_b(value):
    next_value = (value * 48271) % 2147483647

    while next_value % 8 != 0:
        value = next_value
        next_value = (value * 48271) % 2147483647

    return next_value


def main():
    a, b = 699, 124

    final_countdown = 0

    for i in range(5000000):
        a = gen_a(a)
        b = gen_b(b)

        if "".join(format(a, '032b'))[16:] == "".join(format(b, '032b'))[16:]:
            final_countdown += 1

    print(final_countdown)


main()
