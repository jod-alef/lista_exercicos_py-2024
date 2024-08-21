#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
#escrevê-los em ordem crescente.

lst = []
print("Digite 3 números diferentes:")
for i in range(0,3):
    val = int(input())
    
    lst.append(val)
lst.sort()
print(lst)    
