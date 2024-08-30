import sys
import time
import random
from rich import print
from rich.progress import track

def intro():
    print("Olá, este é um programa que sorteia os números da [b]MegaSena[/b]:", ":thumbsup:")
    time.sleep(0.5)
    print(":arrow_right: ","Verifica suas apostas contra os números gerados.")
    time.sleep(0.5)
    print(":arrow_right: ","Verifica os prêmios ganhados.")
    time.sleep(0.5)
    print(":arrow_right: ","Gera e verifica jogos aleatórios contra o resultado.")
    time.sleep(1.5)
    print("[blink][red][b] - Os números do bilhete podem ser digitados ou gerados de forma aleatória -[/b][/red][/blink]")
    principal()

def sorteioMegaSena():
    while True:
        if len(numerosSorteados) == 6:
            break
        else:
            numerosSorteados.add(random.randrange(1,60))

def digitar():
    while len(listaNumeros) != 6:
        print(f"Adicione o {len(listaNumeros)+1}º número: ")
        numeros = int(input(""))
        if numeros > 60:
            print("[red bold]ATENÇÃO[/red bold] -- A mega sena só aceita números menores ou igual a 60")
        elif numeros <= 0:
            print("[red bold]ATENÇÃO[/red bold] -- 0 ou números negativos não são permitidos")
        elif numeros in listaNumeros:
            print("[red bold]ATENÇÃO[/red bold] -- Não são permitidos números repetidos")
        else:
            listaNumeros.add(numeros)
            print(len(listaNumeros))

def nAleatorio():
    while True:
        if len(listaNumeros) == 6:
            break
        else:
            listaNumeros.add(random.randrange(1,60))

def principal():
    while True:
        print("Você gostaria de digitar os números ou que os números sejam sorteados aleatoriamente?")
        print("[bold]Digite [blue]D[/blue] para digitar ou [red]A[/red] para aleatório[/bold]")
        escolha = input("").lower()
        if escolha == "d":
            digitar()
            break
        elif escolha == "a":
            nAleatorio()
            break
        else:
            print("Opção incorreta")

    for i in track(range(10), description="Sorteando os números"):
        time.sleep(0.1)
    sorteioMegaSena()
    print(f"[b]Os números sorteados foram:[red] {sorted(numerosSorteados)}[/b][/red]")
    # Utilizei alguns códigos ANSI escape sequence para melhorar a leitura do terminal.
    time.sleep(1)
    print(f"[b]Os seus números foram[blue] {sorted(listaNumeros)}[/b][/blue]")
    time.sleep(0.5)
    acertos = (numerosSorteados & listaNumeros)
    if len(acertos) == 4:
        print("Parabéns, você ganhou R$ 600,00 na Quadra")
    elif len(acertos) == 5:
        print("Parabéns, você ganhou R$ 15.000,00 na Quina")
    elif len(acertos) == 6:
        print("Você é o mais novo milionário do Brasil com R$ 35Milhões do prêmio máximo da MegaSena,\033[1m PARABÉNS!\033[0m")
    else:
        print(f"Você acertou {len(acertos)} numeros e não ganhou nada, espero que tenha mais sorte da próxima vez")

#Bom lembrar, não dá para declarar set com o formato x = {''} pois o python interpreta como um dictionary, a forma
#correta de declarar sets vazios é utilizando o formato x = set()
listaNumeros = set()
numerosSorteados = set()

while True:
    print("Você gostaria de jogar? (s/n)")
    decisao = input("").lower()
    # LEMBRAR: ao utilizar o or em um if, SEMPRE utilizar parenteses ou checagem fica invalida e sem erros aparentes
    if decisao == "n":
        print("obrigado por utilizar nossos sistemas")
        break
    elif decisao == "s":
        del listaNumeros
        del numerosSorteados
        listaNumeros = set()
        numerosSorteados = set()
        intro()
    else:
        print("Opção invalida")

sys.exit()