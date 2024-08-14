#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
#combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
#dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
#recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia

print("Bom dia, Taxista")
print("Esse é o sistema automatizado de calculo de lucro e consumo de combustível")
print("Favor entrar os dados solicitados:")

kmInicio = int(input("Qual a quilometragem do odometro no inicio do trajeto? "))
kmFinal = int(input("Qual a quilometragem do odometro no final do trajeto? "))
combustivel = int(input("Quantos litros de combustível consumido no trajeto? "))
valor = int(input("Qual o valor total recebido de passageiros? "))

consumo = (kmFinal - kmInicio)/combustivel
lucro = valor - (combustivel * 4.87)

print("Seu consumo médio foi de", consumo,"litros por quilometro")
print("O lucro líquido do dia foi de R$", lucro)