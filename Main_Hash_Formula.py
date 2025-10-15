from Hash_Formula import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    valores_M = [17, 43, 97, 16, 40, 100]

    for M in valores_M:
        hs = HashTable(M)
        with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                hs.inserir(nome)

        freq = hs.size()
        indices = [str(i) for i in range(M)]

        plt.bar(indices, freq)
        plt.xlabel("Índice da tabela hash (0–M-1)")
        plt.ylabel("Quantidade de nomes")
        plt.title(f"Distribuição (Função Hash discutida em aula) — M = {M}")
        plt.show()

        print(f"\nM = {M}")
        print(f"Máx: {max(freq)} colisões | Mín: {min(freq)} colisões")
