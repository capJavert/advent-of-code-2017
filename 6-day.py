import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/DqAj6dGk")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    memory_banks = list(map(int, get_and_prepare_data_string().split("\t")))

    states = [";".join(map(str, memory_banks))]
    steps = 0

    while True:
        current = max(memory_banks)
        index = current_index = memory_banks.index(current)
        memory_banks[current_index] = 0

        while True:
            index = (index+1) % len(memory_banks)

            if current == 0:
                break

            memory_banks[index] += 1
            current -= 1

        list_id = ";".join(map(str, memory_banks))
        steps += 1

        if list_id in states:
            loop_state = list_id
            break

        states.append(list_id)

    states = [loop_state]
    steps = 0

    # and lets just do the same thing again :P

    while True:
        current = max(memory_banks)
        index = current_index = memory_banks.index(current)
        memory_banks[current_index] = 0

        while True:
            index = (index + 1) % len(memory_banks)

            if current == 0:
                break

            memory_banks[index] += 1
            current -= 1

        list_id = ";".join(map(str, memory_banks))
        steps += 1

        if list_id in states:
            break

        states.append(list_id)

    print(steps)


main()
