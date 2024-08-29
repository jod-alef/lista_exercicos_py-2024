import time
import random

print("Olá, este é um programa que lê valores inteiros positivos e:")
time.sleep(0.5)
print("* Encontra o maior e o menor valor.")
time.sleep(0.5)
print("* Calcula a media dos números lidos.")
time.sleep(0.5)
print("* Soma todos os números escolhidos.")
time.sleep(0.5)
print("* Escolhe um número aleatório.")
time.sleep(1.5)
print(" - Os números podem ser digitados ou gerados de forma aleatória -")
quantidadeNumero = int(input("Quantos números você quer adicionar? "))
listaNumeros = []

def digitar():
    for i in range(quantidadeNumero):
        numeros = int(input(f"Insira o {i+1}º numero: "))
        listaNumeros.append(numeros)

def nAleatorio():
    for x in range(quantidadeNumero):
        numeros = random.randrange(1,100)
        listaNumeros.append(numeros)

while True:
    print("Você gostaria de digitar o número ou que os números sejam sorteados aleatoriamente?")
    print("Digite\033[1m d\033[0m para digitar ou\033[1m a\033[0m para aleatório")
    aleatorio = input("")
    if aleatorio == ("d" or "D"):
        digitar()
        break
    elif aleatorio == ("a" or "A"):
        nAleatorio()
        break
    else:
        print("Opção incorreta")


print(f"Os\033[1m números escolhidos\033[0m foram: {listaNumeros}")
listaNumeros.sort()
randomNum = random.choice(listaNumeros)
# Utilizei alguns códigos ANSI escape sequence para melhorar a leitura do terminal.
time.sleep(1)
print(f"O\033[1m menor\033[0m número é {listaNumeros[0]}")
time.sleep(0.5)
print(f"O\033[1m maior\033[0m número é {listaNumeros[-1]}")
time.sleep(0.5)
print(f"A\033[1m média\033[0m de todo6s os números é {sum(listaNumeros)/quantidadeNumero}")
time.sleep(0.5)
print(f"A\033[1m soma\033[0m de todo6s os números é {sum(listaNumeros)}")
time.sleep(0.5)
print(f"O número\033[1m aleatório\033[0m é {randomNum}")
