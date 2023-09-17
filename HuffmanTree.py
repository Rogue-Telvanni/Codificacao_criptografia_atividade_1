class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: str, qtd: int, last: bool):
        # the left sun should never have a son and only the last right node has a value
        # Compare the new value with the parent node
        if self.data:
            self.data += qtd
            if last and self.left:
                self.right = Tree(data)
            elif not self.left:
                self.left.insert(data, qtd + self.data)
                self.right.data = Tree(qtd)
            else:
                self.right.insert(data, qtd + self.data)
        else:
            self.data = qtd
            self.left = Tree(data)

    def search(self, char: str, start_bit_str='') -> str:
        if type(self.data) == int:
            if self.left.data == char:
                return start_bit_str + '0'
            else:
                return self.right.search(char, '1' + start_bit_str)
        elif self.data == char:
            # ultimo valor a direita
            return start_bit_str + '1'
        else:
            return ''
