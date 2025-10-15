class Node:
    def __init__(self, key):
        self.key = key
        self.next = None 

class HashTable:
    def __init__(self, M):
        self.M = M
        self.n = 0
        self.table = [None] * M

    def _hash(self, key):
        return (ord(key[0].upper()) - ord('A')) % self.M

    def inserir(self, key):
        indice = self._hash(key)
        aluno = Node(key)
        aluno.next = self.table[indice]
        self.table[indice] = aluno
        self.n += 1

    def size(self):
        freq = []
        for i in range(self.M):
            total = 0
            aux = self.table[i]
            while aux:
                total += 1
                aux = aux.next
            freq.append(total)
        return freq

    def colisoes(self):
        freq = self.size()
        max_val = max(freq)
        min_val = min(freq)
        letras = [chr(i + 65) for i in range(self.M)]
        letras_mais = [letras[i] for i, v in enumerate(freq) if v == max_val]
        letras_menos = [letras[i] for i, v in enumerate(freq) if v == min_val]
        return letras_mais, max_val, letras_menos, min_val
