# Questões 5 e 6 
# 5) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.
# 6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for
# digitado o valor zero, escrever a palavra zero.
# 
numero = int(input("Entre um numero qualquer e checaremos se é positivo ou negativo: "))

resposta =""
if numero < 0:
    resposta = "negativo"
# ------------ Questão 06 ---------------------
elif numero == 0:
    resposta = "0"
# ---------- Final Questão 06 ------------------
else:
    resposta = "positivo"

print ("O número é", resposta)