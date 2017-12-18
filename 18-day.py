import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/Lv1hb8pF")
    # request = requests.get("https://pastebin.com/raw/PfSAiM0L")
    request.encoding = 'ISO-8859-1'

    return request.text


def is_numeric(value):
    try:
        int(value)

        return True
    except ValueError:
        return False


def main():
    code = get_and_prepare_data_string().splitlines()
    frequency = []
    registers = {chr(i): 0 for i in range(97, 113)}

    index = 0
    while index < len(code):
        command = code[index].split(" ")
        next_index = 1

        if "snd" in command:
            if not is_numeric(command[1]):
                frequency.append(registers[command[1]])
            else:
                frequency.append(command[1])

        if "set" in command:
            if not is_numeric(command[2]):
                registers[command[1]] = registers[command[2]]
            else:
                registers[command[1]] = int(command[2])

        if "add" in command:
            if not is_numeric(command[2]):
                registers[command[1]] += registers[command[2]]
            else:
                registers[command[1]] += int(command[2])

        if "mul" in command:
            if not is_numeric(command[2]):
                registers[command[1]] *= registers[command[2]]
            else:
                registers[command[1]] *= int(command[2])

        if "mod" in command:
            if not is_numeric(command[2]):
                registers[command[1]] %= registers[command[2]]
            else:
                registers[command[1]] %= int(command[2])

        if "rcv" in command:
            if not is_numeric(command[1]):
                value = registers[command[1]]
            else:
                value = int(command[1])

            if value != 0 and len(frequency) > 0:
                print(frequency.pop())
                break

        if "jgz" in command:
            if not is_numeric(command[1]):
                value = registers[command[1]]
            else:
                value = int(command[1])

            if value > 0:
                if not is_numeric(command[2]):
                    next_index = registers[command[2]]
                else:
                    next_index = int(command[2])

        index += next_index


main()
