#Exercicio 7
#A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
#seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
#reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
#voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
#combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
#percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
#abastecimentos é o mesmo.

comprimentoPista = float(input("Insira o comprimento total da pista: "))
numeroVoltas = int(input("Insira o número de voltas a serem percorridas: "))
numeroAbastecimento = int(input("Insira o número de abastecimentos desejado: "))
consumoVeiculo = float(input("Qual o consumo médio do carro em Km/l? "))

litros = (((comprimentoPista/1000) * numeroVoltas)/consumoVeiculo)/numeroAbastecimento

print("Numero mínimo de litros necessário para percorrer até abastecimento", litros)