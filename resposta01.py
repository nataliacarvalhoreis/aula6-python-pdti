#  Tamanho de strings. Faça um programa que leia 2 strings e informe o
# conteúdo delas seguido do seu comprimento. Informe também se as duas
# strings possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.

texto1 = input("Informe o texo 1: ")
texto2 = input("Informe o texto 2: ")

tam1 = len(texto1)
tam2 = len(texto2)

print ("Compara duas strings")
print("String 1: ", texto1)
print("String 2: ", texto2)
print(f"Tamanho de '{texto1}': {tam1} caracteres")
print(f"Tamanho de '{texto2}': {tam2} caracteres")

if tam1 == tam2:
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if texto1 == texto2:
    print("As duas strings são iguais.")
else:
    print("As duas strings são diferentes.")