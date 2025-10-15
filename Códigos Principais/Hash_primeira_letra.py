"""
Hash_primeira_letra.py

    Este arquivo contém uma implementação específica da classe HashTable,
    onde a função de hashing (_hash) é baseada na primeira letra da chave.
    Foi projetado para ser usado em experimentos que exigem este tipo de
    função hash, como a questão 1 e 2 do trabalho.
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None 

class HashTable:
    def __init__(self, M):
        self.M = M #Número de posições da Tabela Hash
        self.n = 0 #Número de chaves na tabela de símbolos
        self.table = [None] * M #Tabela hash

    def _hash(self, key):

        return hash(ord(key[0]) - ord('A')) % self.M

    def inserir (self, key): #Inserir uma chave e valor
        indice = self._hash(key)
        head_list = self.table[indice]

        atual = head_list
        while atual is not None:
            if atual == key:
                return f"A chave {key} já foi adicionada!"
            atual = atual.next

        aluno = Node(key)
        aluno.next = head_list
        self.table[indice] = aluno

        self.n += 1

    def buscar (self, key): #Buscar uma chave
        indice = self._hash(key)
        atual = self.table[indice]

        while atual is not None:
            if atual.key == key:
                return f"A chave {key} foi encontrada!"
            atual = atual.next

    def size (self): #Quantidade de elementos de um único valor
        freq = []
        for i in range(self.M):
            total = 0
            aux = self.table[i]
            if aux == None:
                freq.append(0)
            else:
                while aux is not None:
                    total += 1
                    aux = aux.next
                freq.append(total)
        return freq
    
    def len(self): #Quantidade total de elementos na Tabela hash
        return self.n
    
    def show(self): # mostrar
        for p in range(self.M):
            aux = self.table[p]
            if aux == None:
                print(f"[{p+1}]= null")
            else:
                print(f"[{p+1}]=", end=" ")
                while aux != None:
                    print(f"{aux.key} -", end=" ")
                    aux = aux.next
                print(" null")


