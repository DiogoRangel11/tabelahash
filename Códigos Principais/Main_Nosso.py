# Main_Nosso.py -- versão corrigida (usa rich para um prompt mais bonito)
from Hash_Nosso import HashTable
import matplotlib.pyplot as plt
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import sys

console = Console()

def escolher_tamanho():
    choices = ["16", "17", "26", "40", "43", "97", "100"]
    painel_texto = (
        "[bold cyan]Selecione um número de espalhamento da tabela hash[/bold cyan]\n\n"
        "[bold]Opções:[/bold] " + ", ".join(choices) + "\n\n"
        "Digite o número desejado ou [bold yellow]q[/bold yellow] para sair."
    )
    console.print(Panel(painel_texto, title="Tabela Hash", expand=False))

    while True:
        resposta = Prompt.ask("Escolha", choices=choices + ["q"], default=choices[0])
        if resposta == "q":
            console.print("[red]Saindo...[/red]")
            sys.exit(0)
        try:
            x = int(resposta)
            return x
        except ValueError:
            console.print("[red]Entrada inválida. Tente novamente.[/red]")

def main():
    # escolher tamanho via rich
    x = escolher_tamanho()

    # criar a tabela hash (não alteramos a classe HashTable)
    hs = HashTable(x)

    # ler arquivo e inserir nomes (ignora linhas vazias)
    try:
        with open("alunosED_2025.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                if nome:
                    hs.inserir(nome)
    except FileNotFoundError:
        console.print("[red]Arquivo 'alunosED_2025.txt' não encontrado. Verifique o caminho e tente novamente.[/red]")
        sys.exit(1)

    # obter frequências por bucket
    dados = hs.size()
    console.print("[green]Frequências por bucket:[/green]")
    console.print(dados)

    # informações das colisoes por letra (método da sua classe)
    letras_mais, max_val, letras_menos, min_val = hs.colisoes()
    console.print(f"[bold]Mais frequentes:[/bold] {letras_mais} = {max_val}")
    console.print(f"[bold]Menos frequentes:[/bold] {letras_menos} = {min_val}")

    # preparar rótulos compatíveis com o tamanho de 'dados'
    if len(dados) == 26:
        letras = [chr(65 + i) for i in range(26)]  # A..Z
    else:
        letras = [str(i) for i in range(len(dados))]  # 0..M-1

    # plot
    plt.figure(figsize=(10, 5))
    plt.bar(letras, dados)
    plt.xlabel('Índice da tabela hash (A–Z ou bucket index)')
    plt.ylabel('Frequência')
    plt.title(f'Distribuição de chaves na tabela hash (M = {x})')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
