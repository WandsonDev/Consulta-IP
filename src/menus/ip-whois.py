from requests import get
from json import loads
from time import sleep
import time
import os
import base64



f = '\033[m'
vermelho = '\033[31m'
v = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'

time.sleep(3.2)
os.system("clear");time.sleep(1.5)


def consultar_ip(ip):
    url = f"http://ipwho.is/{ip}?lang=pt-BR"
    response = get(url)
    data = loads(response.text)
    return data

def exibir_dados_ip(data):
    if data["success"]:
        print(f"{amarelo}Dados do IP:")
        print(f"{amarelo}IP: {ciano}{data['ip']}{f}")
        sleep(0.8)

        # Seção Continentes
        print(f"{azul}\nContinentes:")
        print(f"{amarelo}Continente: {ciano}{data['continent']}{f}")
        sleep(0.8)
        print(f"{amarelo}Código do Continente: {ciano}{data['continent_code']}{f}")
        sleep(0.8)

        # Seção País
        print(f"{roxo}\nPaís:")
        print(f"{amarelo}País: {ciano}{data['country']}{f}")
        sleep(0.8)
        print(f"{amarelo}Código do País: {ciano}{data['country_code']}{f}")
        sleep(0.8)

        # Seção Região
        print(f"{ciano}\nRegião:")
        print(f"{amarelo}Região: {ciano}{data['region']}{f}")
        sleep(0.8)
        print(f"{amarelo}Código da Região: {ciano}{data['region_code']}{f}")
        sleep(0.8)

        # Seção Cidade
        print(f"{amarelo}\nCidade:")
        print(f"{amarelo}Cidade: {ciano}{data['city']}{f}")
        sleep(0.8)
        print(f"{amarelo}Latitude: {ciano}{data['latitude']}{f}")
        sleep(0.8)
        print(f"{amarelo}Longitude: {ciano}{data['longitude']}{f}")
        sleep(0.8)

        # Seção Outras Informações
        print(f"{amarelo}\nOutras Informações:")
        print(f"{amarelo}É da União Europeia: {ciano}{data['is_eu']}{f}")
        sleep(0.8)
        print(f"{amarelo}CEP: {ciano}{data['postal']}{f}")
        sleep(0.8)
        print(f"{amarelo}Código de Ligação: {ciano}{data['calling_code']}{f}")
        sleep(0.8)
        print(f"{amarelo}Capital: {ciano}{data['capital']}{f}")
        sleep(0.8)
        print(f"{amarelo}Fronteiras: {ciano}{data['borders']}{f}")
        sleep(0.8)
        print(f"{amarelo}Bandeira: {data['flag']['emoji']}{f}")
        sleep(0.8)

        # Seção Conexão
        print(f"{amarelo}\nConexão:")
        print(f"{amarelo}ASN: {ciano}{data['connection']['asn']}{f}")
        sleep(0.8)
        print(f"{amarelo}Organização: {ciano}{data['connection']['org']}{f}")
        sleep(0.8)
        print(f"{amarelo}ISP: {ciano}{data['connection']['isp']}{f}")
        sleep(0.8)
        print(f"{amarelo}Domínio: {ciano}{data['connection']['domain']}{f}")
        sleep(0.8)

        # Seção Fuso Horário
        print(f"{amarelo}\nFuso Horário:")
        print(f"{amarelo}Fuso Horário: {ciano}{data['timezone']['id']}{f}")
        sleep(0.8)
        print(f"{amarelo}Horário UTC: {ciano}{data['timezone']['utc']}{f}")
        sleep(0.8)
        print(f"{amarelo}Horário Atual: {ciano}{data['timezone']['current_time']}{f}")
        sleep(0.8)

        
        
        sleep(0.8)

while True:
    ip = input("Digite o IP que deseja consultar: ")
    data = consultar_ip(ip)
    exibir_dados_ip(data)

    continuar = input("Deseja fazer outra consulta? (s/n): ")
    if continuar.lower() == "s":
        break
    else:
        os.system("python3 .source/menu/main.py")