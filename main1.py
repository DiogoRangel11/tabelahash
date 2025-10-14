from hash import HashTable
import matplotlib.pyplot as plt

if __name__ == "__main__":
    hs = HashTable(26)

    with open("alunosED_2025.txt", "r", encoding= "utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            hs.inserir(nome)
        freq = hs.size()
        
    # Gerar dados de exemplo
    dados = freq
    print(dados)
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plt.bar(letras, dados)
    plt.xlabel('Índice da tabela hash (A–Z)')
    plt.ylabel('Frequência')
    plt.title('Distribuição de chaves na tabela hash')
    plt.show()


            

            
