#8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

print("Verificador de idade para participar de votação")
idade = int(input("Digite o ano que você nasceu com 4 digitos (ex: 1992): "))

if 2024 - idade < 16:
    naovota = 16 - (2024 - idade)
    print("Você ainda não pode voltar, faltam", naovota, "anos")
else:
    print("Em idade para votar, não esqueça seu título")