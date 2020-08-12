# Nome na vertical em escada invertida. Altere o programa anterior de
# modo que a escada seja invertida.

nome = input("Informe seu nome: ")

tamanho = len(nome)

resposta = ""

for i in range(0, tamanho):
    resposta = resposta + nome[i]

for i in range(0, tamanho):
    j = tamanho - i
    print(resposta[0:j])