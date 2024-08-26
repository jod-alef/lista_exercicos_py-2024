from datetime import date
import time

#8) Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).


def progPrincipal():
    print("Verificador de idade para participar de votação")
    time.sleep(1.5)
    anoNasc = int(input("Digite o ano que você nasceu com 4 digitos (ex: 1992): "))
    idadeUsuario = idade(anoNasc)
    print(verificarVoto(idadeUsuario))
  

def verificarVoto(anosdeVida):
    if anosdeVida < 16:
        naovota = 16 - anosdeVida
        return("Você ainda não pode voltar, faltam", naovota, "anos")
    elif (anosdeVida > 16 and anosdeVida < 18) or anosdeVida > 75:
        return("Você pode votar mas não é obrigatório")
    else:
        return("Em idade para votar, não esqueça seu título de eleitor")

def idade(nascimento):
    return(int(date.today().year - nascimento)) 

progPrincipal()

