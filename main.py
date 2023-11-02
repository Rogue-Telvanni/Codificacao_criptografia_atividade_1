import HuffmanBad
import Golomb
import Elias_Gamma
import Fibonnaci
import Huffman
import CRC
import Cifra_de_Cesar
import BSC

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
    code = Cifra_de_Cesar.cipher_word("arriba", 9)
    print(code)
    print(Cifra_de_Cesar.decipher_word(code, 9))
    print(BSC.add_parity_bits("01011", 3))


    result = CRC.codify("1001")
    print("CRC")
    print(result)

    while True:
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
            (value, tipo) = input_type()
            if tipo == 'txt':
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
        elif choice == '3':
            (value, tipo) = input_type()
            # read file
            if tipo == 'path':
                file = open(value, 'r')
                lines = file.readlines()
                coded_lines = []
                decoded_lines = []
                for line in lines:
                    tree, byte_stream = Huffman.codify(line)
                    coded_lines.append(byte_stream + '\n')
                    decoded_lines.append(Huffman.decodify(tree, byte_stream))

                file.close()
                # write to another file
                write_file = open('huff_out.txt', 'w')
                for code_word in coded_lines:
                    write_file.write(code_word)
                write_file.close()
                print('decodificando')
                for var in decoded_lines:
                    print(var, end="")
            else:
                tree, byte_stream = Huffman.codify(value)
                print(Huffman.decodify(tree, byte_stream))
        elif choice == '4':
            (value, tipo) = input_type(True)
            if tipo == 'txt':
                nums = str(input())
                list_of_number = valida_input(nums, False)
                code = Fibonnaci.codify(list_of_number)
                print('codificação')
                print(code)
                print('decodificicação')
                Fibonnaci.decodify(code)
            else:
                file = open(value, 'r')
                lines = file.readlines()
                for word in lines:
                    list_of_number = valida_input(word, False)
                    code = Fibonnaci.codify(list_of_number)
                    print(code)
                    Fibonnaci.decodify(code)
                file.close()
        elif choice == '5':
            break
        else:
            print("por Favor selecione um valor válido")

    print("programa Finalizado!")


def choices():
    print()
    print("Selecione 0 para codificar um valor de alfabeto com letras e números")
    print("Selecione 1 para codificar um valor de alfabeto de números positivos usando Golomb")
    print("Selecione 2 para codificar um valor de alfabeto de números positivos usando Elias_Gamma")
    print("Selecione 3 para codificar um valor de alfabeto usando huffman")
    print("Selecione 4 para codificar um valor de alfabeto de números usando Fibonnaci")
    print("Selecione 5 para sair")
    print()


def input_type(is_number: bool = False) -> (str, str):
    while True:
        print()
        print("defina o tipo de input")
        print("Selecione 1 para texto")
        print("Selecione 2 para arquivo")
        print()
        valor = str(input())
        if valor == "1":
            if is_number:
                print('digite o alfabeto separando os números com um espaço')
            else:
                print('digite o texto')
            return str(input()), 'txt'
        elif valor == "2":
            try:
                path = str(input())
                f = open(path)
                f.close()
                return path, 'path'
            except FileNotFoundError:
                print('O arquivo não existe!')
        else:
            print('opção inválida')


if __name__ == '__main__':
    main()
