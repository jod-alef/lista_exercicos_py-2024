#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
#compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o valor total da compra.

maca = int(input("Olá, quantas maçãs você gostaria de comprar?"))

if maca < 12:
    compra = maca * 0.30
else:
    compra = maca * 0.25

print("Sua compra ficou R$", compra)