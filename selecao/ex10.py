#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
#escrevê-los em ordem crescente.

valores = []
print("Digite 3 números diferentes:")
for i in range(3):
    val = int(input())
    valores.append(val)
valores.sort()
print(valores)