#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
#escrevê-los em ordem crescente.

lst = []

n = 3
print("Digite 3 números diferentes:")
for i in range(0,n):
    ele = int(input())
    
    lst.append(ele)
lst.sort()
print(lst)    
