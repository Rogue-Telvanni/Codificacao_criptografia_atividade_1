def calculate_fibonacci_code(value: int) -> str:
    byte_str = ''
    previous_value = 1
    next_value = 1
    sequence = [1]
    while True:
        if next_value + previous_value > value:
            break
        else:
            temp = next_value
            next_value = previous_value + next_value
            previous_value = temp
            sequence.append(next_value)

    index = len(sequence) - 1
    soma = 0
    while index >= 0:
        if soma + sequence[index] > value:
            byte_str = '0' + byte_str
        else:
            soma += sequence[index]
            byte_str = '1' + byte_str

        index -= 1
    return byte_str + '1'  # adiciona o stop bit no final


def codify(number_array: []):
    byte_stream = ''
    for value in number_array:
        byte_stream += calculate_fibonacci_code(value)

    print(byte_stream)
    return byte_stream


def decodify(byte_stream: str) -> None:
    counter = 0
    numbers_array = []
    number = 0
    value = 0
    previous = 1
    for index in range(len(byte_stream)):
        char = byte_stream[index]
        if char == '1':
            counter += 1
        else:
            counter = 0

        if counter >= 2:
            numbers_array.append(value)
            previous = 1
            number = 0
            value = 0
            continue

        if number == 0:
            number += previous
            if char == '1':
                value += number
        else:
            temp = number
            number += previous
            previous = temp
            if char == '1':
                value += number

    for i in numbers_array:
        print(i)
