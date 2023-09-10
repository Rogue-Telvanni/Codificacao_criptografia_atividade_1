import math


def dic_create(symbol: str, dict_values: dict) -> None:
    for frq, values in dict_values.items():
        if symbol in values:
            # adiciona um no tamanho do símbolo e adiciona ele ao dicionário
            new_value = frq + 1
            if new_value not in dict_values:
                dict_values[new_value] = []

            dict_values[new_value].append(symbol)
            values.remove(symbol)
            return

    if 1 not in dict_values:
        dict_values[1] = []
    dict_values[1].append(symbol)


def calculate_entropy(dictionary: dict, bits_sizes_dictionary: dict, equal: bool) -> None:
    index = len(dictionary.keys())
    ideal_entropy = 0.0
    calculated_entropy = 0.0
    divisor = 2
    while index >= 1:
        values = dictionary[index]
        if len(values) == 0:
            continue
        ideal_entropy += len(values) * (1 / divisor) * math.log2(divisor)
        divisor = divisor if not equal else math.pow(2, math.ceil(math.log2(len(values))))
        calculated_entropy += len(values) * (1 / divisor) * bits_sizes_dictionary[values[0]]
        # divisor é uma potência de 2 sempre
        divisor *= 2
        index -= 1
    print("Entropia calculada", calculated_entropy)
    print("Entropia ideal", ideal_entropy)


def validate_bits(bit_str: str, uses: []) -> bool:
    if bit_str in uses:
        return False

    for used in uses:
        if len(bit_str) > len(used) and bit_str[:len(used)] == used:
            return False

    return True


def generate_code(values: [], uses: [], coded_values: dict, last_bit_index: int, padding_left_bit: str,
                  words_dict: dict, equal) -> int:
    array_size = len(values)
    index = last_bit_index + 1
    #padding_size = len(padding_left_bit) if not equal else 0
    minimum_bits = math.ceil(math.log2(array_size)) + math.ceil(math.log2(index))
    if minimum_bits == 0:
        minimum_bits = 1
    count = 0
    while True:
        if count >= array_size:
            break
        bit_str = format(index - 1, 'b').rjust(minimum_bits, padding_left_bit)
        while not validate_bits(bit_str, uses):
            index += 1
            bit_str = format(index - 1, 'b').rjust(minimum_bits, padding_left_bit)

        uses.add(bit_str)
        coded_values[bit_str] = values[count]
        words_dict[values[count]] = len(bit_str)
        count += 1
    return index


def codify(value) -> (dict, str):
    dict_values = dict()
    # gera um dicionário e ajusta eles de acordo com a frequência
    for symbol in value:
        dic_create(symbol, dict_values)

    coded_values = dict()
    uses = set()
    words_bits = dict()
    i = len(dict_values.keys())
    last_bit_index = 0
    equal = True if i == 1 else False
    padding = "0"
    while i >= 1:
        values = dict_values[i]
        last_bit_index = generate_code(values, uses, coded_values, last_bit_index, padding, words_bits, equal)
        i -= 1

    stream = ''
    for char in value:
        bits_str = [k for k, v in coded_values.items() if v == char]
        stream += bits_str[0]
    print(stream)
    calculate_entropy(dict_values, words_bits, equal)
    return coded_values, stream


def decodify(dict_code: dict, stream: str) -> None:
    word = ''
    index = 0
    counter = 1
    while index < len(stream):
        if dict_code.get(stream[index: index + counter]) is not None:
            word += dict_code[stream[index: index + counter]]
            index += counter
            counter = 1
        else:
            counter += 1
    print(word)
