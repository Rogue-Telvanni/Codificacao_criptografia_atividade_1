import HuffmanBad
import Golomb
import Elias_Gamma
import Fibonnaci
import Huffman


def valida_input(nums: str, valida_zero: bool) -> []:
    """
    :return an int array or a empty array if there is a problem with the input like not beign a digit
    or not having the correct split char
    """

    new_list = nums.split(' ')
    values_to_codify = []
    for value in new_list:

        if value.isdigit():
            if valida_zero and int(value) == 0:
                return []
            values_to_codify.append(int(value))
        else:
            return []

    return values_to_codify


def main():
    value = 'AKAS'
    tree, byte_stream = Huffman.codify(value)
    Huffman.decodify(tree, byte_stream)

    array = [40]
    code = Fibonnaci.codify(array)
    Fibonnaci.decodify(code)

    choice = ''
    while choice != '4':
        choices()
        choice = str(input())
        if choice == '0':
            print('digite o alfabeto')
            word = str(input())
            print('codificação')
            dict_codes, stream = HuffmanBad.codify(word)
            print('decodificação')
            HuffmanBad.decodify(dict_codes, stream)
        elif choice == '1':
            print('digite o alfabeto separando os números com um espaço')
            nums = str(input())
            list_of_number = valida_input(nums, False)
            if len(list_of_number) < 1:
                print("input inválido")
                continue
            print('codificação')
            k_value, code_words = Golomb.codify(list_of_number)
            print('decodificação')
            Golomb.decodify(code_words, k_value)
        elif choice == '2':
            print('digite o alfabeto separando os números com um espaço e diferente de zero')
            nums = str(input())
            list_of_number = valida_input(nums, True)
            if len(list_of_number) < 1:
                print("input inválido")
                continue
            print('codificação')
            bit_array = Elias_Gamma.codify(list_of_number)
            print('decodificação')
            Elias_Gamma.decodify(bit_array)
        elif choice == '4':
            break
        else:
            print("por Favor selecione um valor válido")

    print("programa Finalizado!")


def choices():
    print()
    print("Selecione 0 para codificar um valor de alfabeto com letras e números")
    print("Selecione 1 para codificar um valor de alfabeto de números positivos usando Golomb")
    print("Selecione 2 para codificar um valor de alfabeto de números positivos usando Elias_Gamma")
    print("Selecione 4 para sair")
    print()


if __name__ == '__main__':
    main()
