from anytree import Node, RenderTree
import requests


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/V1quBdPP")

    request.encoding = 'ISO-8859-1'

    return request.text


"""def f_children(program_name):
    for child in tree[program_name]["p"]:
        Node(child, parent=tree[program_name])
        if len(program["p"]) > 0:
            children(pro)"""


tree = {}


def main():
    raw = get_and_prepare_data_string().splitlines()

    for element in raw:
        element_name = element.split(" ")[0]
        parents = []

        if "->" in element:
            parents = element.split("-> ")[1].split(", ")

        # weight = int(program.split("(")[1].split(")")[0])

        if element_name not in tree:
            tree[element_name] = Node(element_name)

        for parent in parents:
            if parent in tree:
                tree[parent].parent = tree[element_name]
            else:
                tree[parent] = Node(parent, parent=tree[element_name])

    for name, element in tree.items():
        print(RenderTree(element))


main()
