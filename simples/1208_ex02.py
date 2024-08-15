#Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius. (C = (F-32) * 5 / 9)

fahr = input("Qual a temperatura em Fahrenheit?")
f = int(fahr)
c = (f-32)*5/9
print("A temperatura é",c, "gráus celsius")