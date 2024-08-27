"""74) Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem:
“Múltiplo de 10”."""
while True:
    multiplo = int(input("Digite o número que você gostaria de ver os multiplos: "))
    comeco = int(input("Gostaria de começar a contagem de qual número? "))
    final = int(input("Gostaria de terminar a contagem de qual número? "))+1
    if comeco <= final:
        break
    else:
        print("O número de começo é maior que o de final, favor tentar novamente")

for i in range(comeco, final):
    if i % multiplo == 0:
        print(i, "multiplo de", multiplo)
    else:
        print(i)