from Hash_Sistema import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hs = HashTable(26)

    with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            hs.inserir(nome)

    freq = hs.size()
    letras = [chr(i + 65) for i in range(26)]

    plt.bar(letras, freq)
    plt.xlabel("Índice da tabela hash (A–Z)")
    plt.ylabel("Frequência")
    plt.title("Distribuição de chaves (hash interno, M = 26)")
    plt.show()
