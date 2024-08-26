# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
#altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
#paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
#azulejos possui 1,5 m2.

print("Bem vindo a calculadora de gastos de azuleijo")
print("Insira as informações a seguir:")

l = int(input("Largura: "))
c = int(input("Comprimento: "))
a = int(input("Altura: "))


quantidade = (((l*a)*2)+((c*a)*2))/1.5

print("Você vai precisar de ", quantidade," caixas de azulejo")