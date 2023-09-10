import math


def codify(list_of_numbers: []) -> (int, str):
    medium = (max(list_of_numbers) + min(list_of_numbers)) / 2
    k_value = math.ceil(medium)
    suffix = math.ceil(math.log2(medium))
    stop_bit = "1"
    code_words = ''
    dictionary = dict()
    dictionary_sizes = dict()
    for val in list_of_numbers:
        if val < k_value:
            code = stop_bit + format(val, 'b').rjust(suffix, "0")
            code_words = code_words + code
            dic_create(val, dictionary)
            dictionary_sizes[val] = len(code)
        else:
            prefix_number = math.floor(val / k_value)
            prefix = "0" * prefix_number
            binary = format(math.floor(val % k_value), 'b').rjust(suffix, "0")
            code = prefix + stop_bit + binary
            code_words = code_words + code
            dic_create(val, dictionary)
            dictionary_sizes[val] = len(code)

    print(code_words)
    calculate_entropy(dictionary, dictionary_sizes, len(dictionary.keys()) == 1)
    return k_value, code_words


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
        ideal_entropy += len(values) * (1/divisor) * math.log2(divisor)
        divisor = divisor if not equal else math.pow(2, math.ceil(math.log2(len(values))))
        calculated_entropy += len(values) * (1/divisor) * bits_sizes_dictionary[values[0]]
        # divisor é uma potência de 2 sempre
        divisor *= 2
        index -= 1
    print("Entropia calculada", calculated_entropy)
    print("Entropia ideal", ideal_entropy)


def decodify(bit_array, k_value: int) -> None:
    values_array = []
    counter = 0
    size = len(bit_array)
    index = 0
    suffix_size = math.ceil(math.log2(k_value))
    while index < size:
        if bit_array[index] == "1":
            offset = index + 1
            # pega o valor da posição total do sufixo
            bits = bit_array[offset: suffix_size + offset]
            number = counter * k_value + int(bits, 2)
            values_array.append(number)
            index = index + counter + suffix_size
            counter = 0
        else:
            counter += 1

        index += 1

    for result in values_array:
        print(result)
