import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/r3LEuqnG")
    request.encoding = 'ISO-8859-1'

    return request.text


def main():
    particle_data = get_and_prepare_data_string()\
        .replace("p=<", "")\
        .replace("v=<", "")\
        .replace("a=<", "")\
        .replace(">", "")\
        .splitlines()

    particles = {}

    for (index, item) in enumerate(particle_data):
        item = item.split(", ")

        particles[str(index)] = {
            "p": [int(i) for i in item[0].split(",")],
            "v": [int(i) for i in item[1].split(",")],
            "a": [int(i) for i in item[2].split(",")],
        }

    for t in range(100):  # maybe I had luck with this
        collisions = {}

        for i, particle in particles.items():
            particle["v"][0] += particle["a"][0]
            particle["v"][1] += particle["a"][1]
            particle["v"][2] += particle["a"][2]
            particle["p"][0] += particle["v"][0]
            particle["p"][1] += particle["v"][1]
            particle["p"][2] += particle["v"][2]

            particles[i] = particle

            pos = ",".join([str(p) for p in particle["p"]])

            if pos not in collisions:
                collisions[pos] = [i]
            else:
                collisions[pos].append(i)

        for _, group in collisions.items():
            if len(group) > 1:
                for j in group:
                    del particles[j]

    print(len(particles))


main()
