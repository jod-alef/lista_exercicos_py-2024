#Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um
#determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),
#as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é
#de 18 watts por metro quadrado.

potencia = input("Qual a potência das lâmpadas insaladas?")
w = int(potencia)
largura = input("Qual a largura do cômodo? (em metros)")
comprimento = input("Qual a comprimento do cômodo? (em metros)")
l = int(largura)
c = int(comprimento)

#Primeiro calculo a metragem e depois a necessidade total, em watts, da área, dividindo pelos watts das lampadas fornecidas.
metragem = l * c
numero_lampadas = (metragem * 18) / w
print("O número de lampadas necessário são: ", numero_lampadas)