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
        h = 0
        for i in key:
            primeira_letra = key[0]
            h = (ord(primeira_letra) - ord('A')) % self.M
        return h #Retorna o valor somente da primeira Letra

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

    
    def colisoes(self):
    # Inicializa contagem de colisões para cada letra
        contagem = {chr(i + 65): 0 for i in range(26)}  # 'A' a 'Z'

    # percorre todas as posições da tabela hash
        for head in self.table:
            atual = head
            while atual is not None:
                letra = atual.key[0].upper()  # pega a primeira letra da chave
                if letra in contagem:
                    contagem[letra] += 1
                atual = atual.next

    # verifica se a tabela está vazia
        if not contagem:
            return [], 0, [], 0

        max_val = max(contagem.values())
        min_val = min(contagem.values())

        letras_mais = [letra for letra, val in contagem.items() if val == max_val]
        letras_menos = [letra for letra, val in contagem.items() if val == min_val]

        return letras_mais, max_val, letras_menos, min_val


