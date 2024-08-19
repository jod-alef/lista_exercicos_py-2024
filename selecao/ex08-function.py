from datetime import date

#8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

print("Verificador de idade para participar de votação")
idade = int(input("Digite o ano que você nasceu com 4 digitos (ex: 1992): "))

def verificarVoto():
    if date.today().year - idade < 16:
        naovota = 16 - (2024 - idade)
        return("Você ainda não pode voltar, faltam", naovota, "anos")
    else:
        return("Em idade para votar, não esqueça seu título")

print(verificarVoto())