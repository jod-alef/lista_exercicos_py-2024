#7) Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e
#escrever o maior deles.


print("Esse programa vai comparar dois números diferentes e mostrar o maior")
num1 = int(input("Entre um número qualquer:"))
num2 = int(input("Entre outro número (diferente do primeiro): "))

if num1 > num2:
    print(num1)
else:
    print(num2)