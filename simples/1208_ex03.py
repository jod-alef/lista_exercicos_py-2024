# Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor
# correspondente em graus Fahrenheit. (F = (C × 9/5) + 32)

cels = input("Qual a temperatura em Celsius?")
c = int(cels)
f = (c*9/5) + 32
print("A temperatura é",c, " gráus fahrenheit")