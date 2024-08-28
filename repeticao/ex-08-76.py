import time

print("Olá, este é um algoritimo que lê valores inteiros positivos e:")
time.sleep(0.5)
print("* Encontra o maior e o menor valor.")
time.sleep(0.5)
print("* Calcula a media dos números lidos.")
time.sleep(1.5)
quantidadeNumero = int(input("Quantos números você quer adicionar? "))

listaNumeros = []
for i in range(quantidadeNumero):
    numeros = int(input("Insira numero: "))
    listaNumeros.append(numeros)

listaNumeros.sort()
# Utilizei alguns códigos ANSI escape se quence para melhorar a leitura do terminal.
print(f"O\033[1m menor\033[0m número é {listaNumeros[0]}")
print(f"O\033[1m maior\033[0m número é {listaNumeros[-1]}")
print(f"A\033[1m média\033[0m de todo6s os números é {sum(listaNumeros)/quantidadeNumero}")