import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/r3LEuqnG")
    # request = requests.get("https://pastebin.com/raw/R1xLQQfQ")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    particle_data = get_and_prepare_data_string()\
        .replace("p=<", "")\
        .replace("v=<", "")\
        .replace("a=<", "")\
        .replace(">", "")\
        .splitlines()

    closest = (None, None)

    for (index, item) in enumerate(particle_data):
        item = item.split(", ")

        particle = {
            "p": [int(i) for i in item[0].split(",")],
            "v": [int(i) for i in item[1].split(",")],
            "a": [int(i) for i in item[2].split(",")]
        }

        movement = (abs(particle["a"][0])+abs(particle["a"][1])+abs(particle["a"][2])) * \
                   (abs(particle["v"][0])+abs(particle["v"][1])+abs(particle["v"][2]))

        if movement < closest[1] or closest[1] is None:
            closest = (index, movement)

    print(closest[0])


main()
