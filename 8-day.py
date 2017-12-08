import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/Fn0maXDk")
    request.encoding = 'ISO-8859-1'

    return request.text


registers = {}


def main():
    instructions = get_and_prepare_data_string().splitlines()

    for i in range(len(instructions)):
        inst = instructions[i].split(" ")

        if inst[0] not in registers:
            registers[inst[0]] = 0

        if inst[4] not in registers:
            registers[inst[4]] = 0

    for i in range(len(instructions)):
        inst = instructions[i].split(" ")

        if "inc" in inst:
            operator = "+="
        else:
            operator = "-="

        exec(
            'registers["'+inst[0]+'"]'+operator+inst[2]+' if '+'registers["'+inst[4]+'"] '+' '.join(inst[5:])+' else 0'
        )

    print(registers[max(registers, key=registers.get)])


main()
