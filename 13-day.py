import requests
import copy


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/0kjSuzNx")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    records = get_and_prepare_data_string().splitlines()
    layers = {r.split(": ")[0]: {"range": int(r.split(": ")[1]), "position": 0, "direction": True} for r in records}
    cached = copy.deepcopy(layers)

    busted = False
    delay = 0

    while True:
        if delay > 0:
            layers = copy.deepcopy(cached)

            for key in layers.keys():
                layers[key]["position"] += 1 if layers[key]["direction"] else -1

                if layers[key]["position"] == layers[key]["range"] - 1 or layers[key]["position"] == 0:
                    layers[key]["direction"] = not layers[key]["direction"]

        cached = copy.deepcopy(layers)

        for i in range(int(records[-1].split(": ")[0])+1):
            current = str(i)
            if current in layers:
                if layers[current]["position"] == 0:
                    busted = True
                    break

            for key in layers.keys():
                layers[key]["position"] += 1 if layers[key]["direction"] else -1

                if layers[key]["position"] == layers[key]["range"] - 1 or layers[key]["position"] == 0:
                    layers[key]["direction"] = not layers[key]["direction"]

        if busted:
            busted = False
            delay += 1
        else:
            break

    print(delay)


main()
