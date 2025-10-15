"""
    Main_primeira_letra.py

    Este script principal executa o experimento focado na questão 1 do
    trabalho. Ele lê os nomes do arquivo de alunos, insere-os em uma
    tabela hash com M=26 e uma função de hash baseada na primeira letra,
    e, em seguida, gera um histograma da distribuição.
"""

from Hash_primeira_letra import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hs = HashTable(26)

    with open("alunosED_2025.txt", "r", encoding= "utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            hs.inserir(nome)
        freq = hs.size()
    dados = freq
    print(dados)
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plt.bar(letras, dados)
    plt.xlabel('Índice da tabela hash (A–Z)')
    plt.ylabel('Frequência')
    plt.title('Distribuição de chaves na tabela hash')
    plt.show()


            

            

