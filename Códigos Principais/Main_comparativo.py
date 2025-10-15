"""
Main_comparativo.py

    Este script principal executa os experimentos de tabelas hash com
    diferentes valores de M (primos e não-primos) para analisar a
    distribuição e o espalhamento dos dados. Ele utiliza a função hash
    discutida em sala de aula para comparar o desempenho e responder às
    questões 3 e 4 do trabalho.
"""

from Hash_tabela_encadeamento import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    numeros_de_teste = [16, 17, 26, 40, 43, 97, 100]

    try:
        menu = "Selecione um numero de espalhamento da tabela hash \n 16-17-26-40-43-97-100\n"
        x = int(input(menu))

        if x not in numeros_de_teste:
            raise ValueError("Valor Fora da Lista")
        
        hs = HashTable(x)

    except ValueError:
        print("Digite um numero dos mostrados!!")

    with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            hs.inserir(nome)
        
        freq = hs.size()
    
    dados = freq
    print(dados)

    letras_mais, max_val, letras_menos, min_val = hs.colisoes()
    print(letras_mais, max_val, letras_menos, min_val)

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plt.bar(letras, dados)
    plt.xlabel('Índice da tabela hash (A–Z)')
    plt.ylabel('Frequência')
    plt.title('Distribuição de chaves na tabela hash')
    plt.show()
