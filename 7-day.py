import requests
from anytree import Node, RenderTree, PreOrderIter


def get_and_prepare_data_string():
    """
    fetch data for my user from pastebin
    """

    request = requests.get("https://pastebin.com/raw/V1quBdPP")

    request.encoding = 'ISO-8859-1'

    return request.text


def calculate_balance(element_name, prefix="", visual_mode=False, break_filter=None, parse_filter=None):
    if parse_filter:
        if element_name not in parse_filter:
            return

    if break_filter:
        if prefix.count("\t") > break_filter:
            return

    if visual_mode:
        print(prefix+str(prefix.count("\t"))+". "+element_name+": "+str(weights[element_name]))
        prefix += "\t"

    for element in tree[element_name]["p"]:
        calculate_balance(element, prefix, visual_mode=visual_mode, break_filter=break_filter,
                          parse_filter=parse_filter)


def build_tree(element_name, parent=None, parse_filter=None):
    if parse_filter:
        if element_name not in parse_filter:
            return

    if parent:
        node_tree[element_name] = Node(element_name, parent=parent)
    else:
        node_tree[element_name] = Node(element_name)

    for element in tree[element_name]["p"]:
        node_tree[element] = Node(element, node_tree[element_name])
        build_tree(element, node_tree[element], parse_filter=parse_filter)


def check_balance(element_name, parent=None):
    if element_name not in weights:
        weights[element_name] = 0

    if parent:
        if parent not in weights:
            weights[parent] = 0

    if parent:
        weights[parent] += tree[element_name]["w"]

    weights[element_name] += tree[element_name]["w"]

    for element in tree[element_name]["p"]:
        if parent:
            weights[parent] += tree[element]["w"]
        else:
            weights[element_name] += tree[element]["w"]

        check_balance(element, element_name)


def parse_tree(raw, parse_filter=None):
    for element in raw:
        element_name = element.split(" ")[0]

        if parse_filter:
            if element_name not in parse_filter:
                continue

        parents = []

        if "->" in element:
            parents = element.split("-> ")[1].split(", ")

        weight = int(element.split("(")[1].split(")")[0])

        tree[element_name] = {"w": weight, "p": parents}


weights = {}
tree = {}
node_tree = {}


def main():
    raw = get_and_prepare_data_string().splitlines()
    bottom = "ykpsek"  # check my solution for part 1

    parse_tree(raw)

    # calculate_balance(bottom)

    # print(weights)

    build_tree(bottom)
    # print(RenderTree(node_tree["tknk"]))

    check_balance(bottom)

    # calculate_balance(bottom, visual_mode=True, break_filter=None)

    invalid_elements = []

    for node in PreOrderIter(node_tree[bottom]):
        name = node.name.split("/")[-1]

        elements = []
        for child in tree[name]["p"]:
            elements.append(weights[child])

        if elements[1:] != elements[:-1]:
            invalid_elements.append(name)
            # print(name, elements)
            # print(name, False)

    # parse_tree(raw, parse_filter=invalid_elements)

    print(invalid_elements)

    build_tree(invalid_elements[0], parse_filter=invalid_elements)

    for pre, fill, node in RenderTree(node_tree["uduyfo"]):
        print("%s%s (%s)" % (pre, node.name, str(weights[node.name.split("/")[-1]])))

    # calculate_balance(invalid_elements[0], visual_mode=True, parse_filter=invalid_elements)

    for element in tree["uduyfo"]["p"]:
        print(element, tree[element]["w"])


main()
