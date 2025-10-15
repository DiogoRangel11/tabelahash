from Hash_PorLetra import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hs = HashTable(26)

    with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            hs.inserir(nome)

    freq = hs.size()
    letras_mais, max_val, letras_menos, min_val = hs.colisoes()

    print(f"Letras com mais colisões: {letras_mais} → {max_val}")
    print(f"Letras com menos colisões: {letras_menos} → {min_val}")

    letras = [chr(i + 65) for i in range(26)]
    plt.bar(letras, freq)
    plt.xlabel("Letra inicial do nome")
    plt.ylabel("Quantidade de nomes")
    plt.title("Distribuição por primeira letra (M = 26)")
    plt.show()
