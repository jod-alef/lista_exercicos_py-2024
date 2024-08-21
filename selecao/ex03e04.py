''' 
3) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
aluno foi aprovado (considere 6.0 a média mínima para aprovação).
4) Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
média calculada seja menor que 6.0. 
'''

def entradaNotas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/2
    
    if media < 6.0:
        print("Você foi REPROVADO!")
    else:
        print("PARABÉNS! Você foi aprovado!")

while True:
    resposta = input("Você gostaria de inserir novas notas (s/n)")
    if resposta == ("n" or "N"):
        print("Obrigado por utilizar o sistema de calculo de aprovação")
        break
    else:
        entradaNotas()
