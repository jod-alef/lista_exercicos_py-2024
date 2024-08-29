import sys
import time
import random
def intro():
    print("Olá, este é um programa que sorteia os números da MegaSena:")
    time.sleep(0.5)
    print("* Verifica suas apostas contra os números gerados.")
    time.sleep(0.5)
    print("* Verifica os prêmios ganhados.")
    time.sleep(0.5)
    print("* Gera e verifica jogos aleatórios contra o resultado.")
    time.sleep(1.5)
    print(" - Os números do bilhete podem ser digitados ou gerados de forma aleatória -")
    listaNumeros = set()
    #Bom lembrar, não dá para declarar set com o formato x = {''} pois o python interpreta como um dictionary, a forma
    #correta de declarar sets vazios é utilizando o formato x = set()
    numerosSorteados = set()
    principal()

def sorteioMegaSena():
    while True:
        if len(numerosSorteados) == 6:
            break
        else:
            numerosSorteados.add(random.randrange(1,60))

def digitar():
    while True:
        numeros = int(input(f"Insira o numero: "))
        if numeros > 60:
            print("A mega sena só aceita números menores ou igual a 60")
        elif numeros <= 0:
            print("0 ou números negativos não são permitidos")
        elif numeros in listaNumeros:
            print("Não são permitidos números repetidos")
        elif len(listaNumeros) == 6:
            break
        else:
            listaNumeros.add(numeros)

def nAleatorio():
    while True:
        if len(listaNumeros) == 6:
            break
        else:
            listaNumeros.add(random.randrange(1,60))

def principal():
    while True:
        print("Você gostaria de digitar os números ou que os números sejam sorteados aleatoriamente?")
        print("Digite\033[1m d\033[0m para digitar ou\033[1m a\033[0m para aleatório")
        escolha = input("")
        if escolha == ("d" or "D"):
            digitar()
            break
        elif escolha == ("a" or "A"):
            nAleatorio()
            break
        else:
            print("Opção incorreta")

    print('Sorteando os números')
    for i in range(5):
        print(".")
        time.sleep(0.1)
    sorteioMegaSena()
    print(f"Os\033[1m números sorteados\033[0m foram: {numerosSorteados}")
    # Utilizei alguns códigos ANSI escape sequence para melhorar a leitura do terminal.
    time.sleep(1)
    print(f"Os\033[1m seus números\033[0m foram {listaNumeros}")
    time.sleep(0.5)
    acertos = len(numerosSorteados ^ listaNumeros)
    if acertos == 4:
        print("Parabéns, você ganhou R$ 600,00 na Quadra")
    elif acertos == 5:
        print("Parabéns, você ganhou R$ 15.000,00 na Quina")
    elif acertos == 6:
        print("Você é o mais novo milionário do Brasil com R$ 35Milhões do prêmio máximo da MegaSena,\033[1m PARABÉNS!\033[0m")
    else:
        print("Você não ganhou nada, espero que tenha mais sorte da próxima vez")
listaNumeros = set()
#Bom lembrar, não dá para declarar set com o formato x = {''} pois o python interpreta como um dictionary, a forma
#correta de declarar sets vazios é utilizando o formato x = set()
numerosSorteados = set()
while True:
    print("Você gostaria de jogar? (s/n)")
    decisao = input("")
    # LEMBRAR: ao utilizar o or em um if, SEMPRE utilizar parenteses ou checagem fica invalida e sem erros aparentes
    if decisao == ("n" or "N"):
        print("obrigado por utilizar nossos sistemas")
        break
    elif decisao == ("s" or "S"):
        del listaNumeros
        del numerosSorteados
        listaNumeros = set()
        numerosSorteados = set()
        intro()
    else:
        print("Opção invalida")
sys.exit()