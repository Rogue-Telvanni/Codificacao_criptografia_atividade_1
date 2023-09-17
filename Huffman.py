import HuffmanTree
from collections import OrderedDict


def generate_tree(sorted_symbols: OrderedDict):
    tree = None
    index = 0
    for key, value in sorted_symbols.items():
        if not tree:
            tree = HuffmanTree.Tree(0)

        tree.insert(key, value, index == len(sorted_symbols.items()) - 1)
        index += 1

    return tree


def generate_bytes(tree: HuffmanTree.Tree, char: str) -> str:
    return_value = tree.search(char)
    return return_value


def codify(symbols: str) -> (HuffmanTree.Tree, str):
    symbols_counter = dict()
    for symbol in symbols:
        if symbol not in symbols_counter:
            symbols_counter[symbol] = 1
        else:
            symbols_counter[symbol] = symbols_counter[symbol] + 1

    sorted_symbols = OrderedDict(sorted(symbols_counter.items(), key=lambda x: x[1], reverse=True))
    tree = generate_tree(sorted_symbols)
    byte_stream = ''
    for char in symbols:
        byte_stream += generate_bytes(tree, char)
    return tree, byte_stream


def decodify(tree: HuffmanTree.Tree, byte_stream: str) -> None:
    string = ''

    print(string)