
def main():
    n = 355
    buffer = [0]
    p = 0

    for i in range(1, 2018):
        p = (p + n) % len(buffer)
        buffer.insert(p+1, i)
        p += 1

    print(buffer[p+1])


main()
