
def main():
    n = 355
    buffer = 1
    p = 0
    resolver = None

    for i in range(1, 50000000):
        p = (p + n) % buffer
        if p == 0:
            resolver = i

        buffer += 1
        p += 1

    print(resolver)


main()
