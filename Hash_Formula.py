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
        h = 0
        for c in key:
            h = (31 * h + ord(c)) % self.M
        return h

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
