# Data por extenso. Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
# extenso.

def nome(mes):
    numero_mes = int(mes)
    meses = ['janeiro', 'fevereiro', 'março', 'abril',
             'maio', 'junho', 'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro']
    return meses[numero_mes-1]

def eh_valida(data):
    return True

data = input("Data de nascimento: ")

elementos = data.split("/")

print(f"Você nasceu em {elementos[0]} de {nome(elementos[1])} de {elementos[2]}")