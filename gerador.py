# 
#      Gerador de email e senhas
#    
# 

import random
import string
import os

#função para gerar senha
def gerar_senha():

    tamanho_senha = 6

    senha_aleatoria = ''.join(random.choice(string.ascii_letters + string.digits) for _ in
    range(tamanho_senha))
    print(senha_aleatoria)

#função para gerar email
def gerar_email():
    tamanho_do_email = 8
    email_aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in
    range(tamanho_do_email))

    email_final = email_aleatorio + "@gmail.com"

    print(email_final)


# Parte Principal do Programa 
os.system("title Gerador 2.0")

print("GERADOR")
print('\n------------------------------------------\n')
print(' ESCOLHA UMA DAS OPÇÕES ABAIXO')
print(' 1 - GERAR SENHA ')
print(' 2 - GERAR EMAIL\n')
print('-------------------------------------------\n')

opcao = int(input(">_  "))

if opcao == 1:

    print("\nsua senha é ")
    gerar_senha()
    print("")


elif opcao == 2:
    print("\nseu email é ")
    gerar_email()
    print("")

else:

    print("\nOpção INVALIDA")

os.system("pause")

