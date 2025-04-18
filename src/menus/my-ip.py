from requests import get
from json import loads
from time import sleep

f = '\033[m'
vermelho = '\033[31m'
v = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'

def consultar_ip():
    url = "https://api.myip.com"
    response = get(url)
    data = loads(response.text)
    return data

def exibir_dados_ip(data):
    print(f"{amarelo}Dados do seu IP:")
    print(f"{amarelo}IP: {ciano}{data['ip']}{f}")
    sleep(0.8)
    print(f"{amarelo}País: {ciano}{data['country']}{f}")
    sleep(0.8)
    print(f"{amarelo}Código do País: {ciano}{data['cc']}{f}")
    sleep(0.8)

while True:
    data = consultar_ip()
    exibir_dados_ip(data)

    continuar = input("Deseja fazer outra consulta? (s/n): ")
    if continuar.lower() == "s":
        break
    else:
        os.system("python3 src/menu/main.py")
