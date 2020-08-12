# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é
# idêntica se feita da direita para esquerda ou vice−versa. Por exemplo:
# OSSO e OVO são palíndromos. Em textos mais complexos os espaços e
# pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma
# frase palíndroma onde os espaços foram ignorados. Faça um programa
# que leia uma seqüência de caracteres, mostre−a e diga se é um
# palíndromo ou não

texto = input("Informe a frase a ser analisada: ")

texto = texto.replace(" ", "")
texto = texto.upper()
texto2 = texto[len(texto)::-1]

if texto == texto2:
    print("É um palíndromo!")
else:
    print("Não é um palindromo!")