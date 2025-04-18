from os import execl;from sys import argv, executable
from time import sleep
import time
import os
import random

def restart():                              
    execl(executable, executable, *argv)    
 
f = '\033[m';vermelho = '\033[31m';v = '\033[32m';amarelo = '\033[33m';azul = '\033[34m';roxo = '\033[35m';ciano = '\033[36m'
error = (f'  {vermelho}[ X ] ')

sucess = (f' {amarelo}[ ▪ ] ')

pr_ip = f'{amarelo}[ ? ] {ciano} Digite o IP à Ser Consultado:\n--> {amarelo}'



from requests import get
from json import loads
time.sleep(3.2)
os.system("clear");time.sleep(1.5)


def consultar_ip(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=pt-BR"
    response = get(url)
    data = loads(response.text)
    return data

def exibir_dados_ip(data):
    if data["status"] == "success":
        print(f"{amarelo}Dados do IP:");time.sleep(0.8)
        print(f"{amarelo}IP: {ciano}{data['query']}{f}");time.sleep(0.8)
        print(f"{amarelo}Continente: {ciano}{data['continent']}{f}");time.sleep(0.8)
        print(f"{amarelo}Código do Continente: {ciano}{data['continentCode']}{f}");time.sleep(0.8)
        print(f"{amarelo}País: {ciano}{data['country']}{f}");time.sleep(0.8)
        print(f"{amarelo}Código do País: {ciano}{data['countryCode']}{f}");time.sleep(0.8)
        print(f"{amarelo}Região: {ciano}{data['region']}{f}");time.sleep(0.8)
        print(f"{amarelo}Nome da Região: {ciano}{data['regionName']}{f}");time.sleep(0.8)
        print(f"{amarelo}Cidade: {ciano}{data['city']}{f}");time.sleep(0.8)
        print(f"{amarelo}Distrito: {ciano}{data['district']}{f}");time.sleep(0.8)
        print(f"{amarelo}CEP: {ciano}{data['zip']}{f}");time.sleep(0.8)
        print(f"{amarelo}Latitude: {ciano}{data['lat']}{f}");time.sleep(0.8)
        print(f"{amarelo}Longitude: {ciano}{data['lon']}{f}");time.sleep(0.8)
        print(f"{amarelo}Fuso Horário: {ciano}{data['timezone']}{f}");time.sleep(0.8)
        print(f"{amarelo}Offset: {ciano}{data['offset']}{f}");time.sleep(0.8)
        print(f"{amarelo}Moeda: {ciano}{data['currency']}{f}");time.sleep(0.8)
        print(f"{amarelo}ISP: {ciano}{data['isp']}{f}");time.sleep(0.8)
        print(f"{amarelo}Organização: {ciano}{data['org']}{f}");time.sleep(0.8)
        print(f"{amarelo}AS: {ciano}{data['as']}{f}");time.sleep(0.8)
        print(f"{amarelo}Nome AS: {ciano}{data['asname']}{f}");time.sleep(0.8)
        print(f"{amarelo}Reverse DNS: {ciano}{data['reverse']}{f}");time.sleep(0.8)
        print(f"{amarelo}É Móvel: {ciano}{data['mobile']}{f}");time.sleep(0.8)
        print(f"{amarelo}É Proxy: {ciano}{data['proxy']}{f}");time.sleep(0.8)
        print(f"{amarelo}É Hospedagem: {ciano}{data['hosting']}{f}");time.sleep(0.8)
    else:
        print(f"{vermelho}Não foi possível obter os dados do {ciano}IP.{f}")

# Consulta o IP
ip = input(pr_ip)
dados_ip = consultar_ip(ip)

# Exibe os dados
exibir_dados_ip(dados_ip)

# Pergunta se deseja fazer uma nova consulta

opcao = input(f"\n{amarelo}Deseja fazer uma nova consulta? (s/n): ")
if opcao.lower() == "s":
    novo_ip = input(f"{amarelo}Digite o novo IP: ")
    dados_novo_ip = consultar_ip(novo_ip)
    exibir_dados_ip(dados_novo_ip)
else:
    print(f"{ciano}Consulta encerrada.")
    os.system("python3 .source/menu/index.py")

