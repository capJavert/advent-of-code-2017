import requests
from anytree import Node


def gpds():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/teuiA3qF")
    request.encoding = 'ISO-8859-1'

    return request.text


pipes = []
groups = []


def into_the_pipe(group):
    history = list(group)

    for p in pipes:
        if any(d['p'] == p for d in history):
            continue

        tg = list(group)

        if p[0] == history[-1]["c"]:
            node = {"n": Node(p[0] + "-" + p[1], parent=history[-1]["n"]), "p": p, "c": p[1],
                    "v": history[-1]["v"] + int(p[0]) + int(p[1])}

            tg.append(node)
            groups.append(node)
            into_the_pipe(list(tg))

        if p[1] == history[-1]["c"]:
            node = {"n": Node(p[0] + "-" + p[1], parent=history[-1]["n"]), "p": p, "c": p[0],
                    "v": history[-1]["v"] + int(p[0]) + int(p[1])}

            tg.append(node)
            groups.append(node)
            into_the_pipe(list(tg))


def main():
    global pipes
    pipes = [component.split("/") for component in gpds().splitlines()]

    for pipe in pipes:
        try:
            index = pipe.index('0')
        except:
            continue

        group = [{"n": Node(pipe[0]+"-"+pipe[1]), "p": pipe, "c": pipe[0] if index == 1 else pipe[1],
                  "v": int(pipe[0])+int(pipe[1])}]

        into_the_pipe(group)

    maxv = 0
    maxdv = 0
    maxd = 0

    for node in groups:
        if node["v"] > maxv:
            maxv = node["v"]

        c = str(node["n"]).count("/")

        if c > maxd:
            maxd = c
            maxdv = node["v"]
        elif c == maxd:
            if node["v"] > maxdv:
                maxd = c
                maxdv = node["v"]

    print(maxv, maxdv)


main()
