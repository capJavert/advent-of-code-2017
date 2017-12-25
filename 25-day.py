from collections import Counter


def main():
    infinity_tape = {}
    state = "A"
    p = 0

    for _ in range(12523873):
        if p not in infinity_tape:
            infinity_tape[p] = 0

        if state == "A":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p += 1
                state = "B"
            else:
                infinity_tape[p] = 1
                p -= 1
                state = "E"
        elif state == "B":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p += 1
                state = "C"
            else:
                infinity_tape[p] = 1
                p += 1
                state = "F"
        elif state == "C":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p -= 1
                state = "D"
            else:
                infinity_tape[p] = 0
                p += 1
                state = "B"
        elif state == "D":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p += 1
                state = "E"
            else:
                infinity_tape[p] = 0
                p -= 1
                state = "C"
        elif state == "E":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p -= 1
                state = "A"
            else:
                infinity_tape[p] = 0
                p += 1
                state = "D"
        elif state == "F":
            if infinity_tape[p] == 0:
                infinity_tape[p] = 1
                p += 1
                state = "A"
            else:
                infinity_tape[p] = 1
                p += 1
                state = "C"

    print(Counter(infinity_tape.values())[1])


main()
