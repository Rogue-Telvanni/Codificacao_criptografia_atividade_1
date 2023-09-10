import math


def codify(list_of_numbers):
    bit_array = ""
    stop_bit = "1"
    for val in list_of_numbers:
        if val == 1:
            bit_array = bit_array + "1"
            continue
        prefix_size = math.floor(math.log2(val))
        prefix = "0" * prefix_size
        number = val - math.ceil(math.pow(2, prefix_size))
        suffix = format(number, 'b').rjust(prefix_size, "0")
        data = prefix + stop_bit + suffix
        bit_array = bit_array + data

    print(bit_array)
    return bit_array


def decodify(bit_array):
    values_array = []
    counter = 0
    size = len(bit_array)
    index = 0
    while index < size:
        if bit_array[index] == "1":
            if counter == 0:
                values_array.append(1)
                index += 1
                continue

            offset = index + 1
            bit = bit_array[offset: counter + offset]
            log = math.ceil(math.pow(2, counter))
            number = log + int(bit, 2)
            values_array.append(number)
            index = index + counter
            counter = 0
        else:
            counter += 1

        index += 1

    for result in values_array:
        print(result)
