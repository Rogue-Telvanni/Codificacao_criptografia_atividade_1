def codify(byte_stream: str) -> str:
    divisor = '1011'
    reminder = "000"
    index = 0
    validator = byte_stream + reminder
    result = validator[index: len(divisor)]
    while True:
        if result[0: 1] == "1":
            result = bytes_to_xor(result[1:], divisor[1:])
        else:
            result = bytes_to_xor(result[1:], ("0".rjust(len(divisor) - 1, "0")))

        if index + 1 + len(divisor) > len(validator):
            break

        result += validator[len(divisor) + index: len(divisor) + index + 1]
        index += 1

    value = byte_stream + result
    return value


def bytes_to_xor(byte: str, divisor: str) -> str:
    result = ""
    for i in range(len(byte)):
        if byte[i: i + 1] == divisor[i: i + 1]:
            result += "0"
        else:
            result += "1"

    return result
