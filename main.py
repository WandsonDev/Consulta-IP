from os import execl;from sys import argv, executable
from time import sleep
import time
import os
import random
import sys

def restart():                              
    execl(executable, executable, *argv)    
 
f = '\033[m';vermelho = '\033[31m';v = '\033[32m';amarelo = '\033[33m';azul = '\033[34m';roxo = '\033[35m';ciano = '\033[36m'

from requests import get
from json import loads
time.sleep(3.2)
os.system("clear");time.sleep(1.5)

logoa = '.source/logo/logo.txt'
apps = '.source/menu/main.py'

with open(logoa, 'r') as file:
    conteudo = file.read()

print(f"{vermelho}{conteudo}");time.sleep(2.3);


def verificar_usuario():
    # Verifica se o arquivo de nome de usuário existe
    return os.path.exists('.source/userdata/username.txt')
    os.system("cd .source/main.py")

def criar_usuario():
    # Solicita o nome de usuário e a senha ao usuário
    username = input(f'{amarelo}Como Gostaria de Ser Chamando?\n-->{ciano} ')
    senha = input(f'\n{amarelo}Como Vai Ser Sua Senha de Acesso à Este Script?\n-->{ciano} ')

    # Salva o nome de usuário em um arquivo
    with open('.source/userdata/username.txt', 'w') as arquivo_username:
        arquivo_username.write(username)

    # Salva a senha em um arquivo
    with open('.source/userdata/senha.txt', 'w') as arquivo_senha:
        arquivo_senha.write(senha)

    print("Usuario Criado. Abrindo Script...")
    os.system(f'python3 {apps}')

def main():
    if verificar_usuario():
    
        os.system("clear");print(f"{vermelho}{conteudo}");time.sleep(2.3);
        with open('.source/userdata/username.txt', 'r') as arquivo_username:
            username = arquivo_username.read().strip()
            
        if len(sys.argv) > 1:
          print(f'{amarelo}Foi Detectado que Você Colocou Algo Após o \"python3 start.py\". Vamos Verificar se Foi Sua{ciano} Senha!');time.sleep(2.5)
          senha_armazenada = sys.argv[1]
          
        else:
          senha_armazenada = input(f'{ciano}Eae {username}, Digite sua senha para continuar:\n-->{amarelo} ')

        with open('.source/userdata/senha.txt', 'r') as arquivo_senha:
            senha_salva = arquivo_senha.read().strip()

        if senha_armazenada == senha_salva:
    
            print(f'{ciano}Senha correta! Continuando...')
            os.system(f'python3 {apps}')
            # Adicione aqui a lógica para continuar o programa

        else:
            print("Senha incorreta. Tente novamente.")
            restart()

    else:
        print("Usuário não encontrado.")
        criar_usuario()

if __name__ == "__main__":
    main()

