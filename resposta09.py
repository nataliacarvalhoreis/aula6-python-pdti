# Verificação de CPF. Desenvolva um programa que solicite a digitação de
# um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número
# válido ou inválido através da validação dos dígitos verificadores e dos
# caracteres de formatação.

def validar_formato(cpf):
    #XXX.XXX.XX-XX
    if (cpf[3] != ".") or (cpf[7] != ".") or (cpf[11] != "-"):
        return False
    else:
        return True

def validar_cpf(cpf):
    if validar_formato(cpf):
        cpf_limpo = cpf.replace('.','').replace('-','')
        contador = 10
        soma = 0
        for caractere in cpf_limpo:
            if contador > 1:
                soma += int(caractere) * contador
                contador -= 1

        digito1 = (soma * 10) % 11

        if digito1 != int(cpf_limpo[9]):
            return False

        contador = 11
        soma = 0
        for caractere in cpf_limpo:
            if contador > 1:
                soma += int(caractere) * contador
                contador -= 1
        digito2 = (soma * 10) % 11

        if digito2 != int(cpf_limpo[10]):
            return False
    else:
        return False

    return True

#testes
cpf = input("CPF(xxx.xxx.xxx-xx) :")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")

