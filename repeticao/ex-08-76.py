import time

print("Bem vind@, este é um algoritimo que lê 50 valores inteiros positivos e:")
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
print(f"O menor número é", listaNumeros[0])
print(f"O menor número é", listaNumeros[-1])
print(f"A soma de todos os números é", sum(listaNumeros))