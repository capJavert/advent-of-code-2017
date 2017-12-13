import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/0kjSuzNx")
    # request = requests.get("https://pastebin.com/raw/LThCe14f")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    records = get_and_prepare_data_string().splitlines()
    layers = {r.split(": ")[0]: int(r.split(": ")[1]) for r in records}

    severity = 0

    for i in range(int(records[-1].split(": ")[0])+1):
        if str(i) in layers:
            firewall_index = 0
            direction = True
            for j in range(i):
                firewall_index += 1 if direction else -1

                if firewall_index == layers[str(i)]-1 or firewall_index == 0:
                    direction = not direction

            if firewall_index == 0:
                severity += int(i)*layers[str(i)]

    print(severity)


main()
