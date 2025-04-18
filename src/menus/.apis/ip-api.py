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
        print(f"{amarelo}Dados do IP:")
        print(f"{amarelo}IP: {ciano}{data['query']}{f}")
        print(f"{amarelo}Continente: {ciano}{data['continent']}{f}")
        print(f"{amarelo}Código do Continente: {ciano}{data['continentCode']}{f}")
        print(f"{amarelo}País: {ciano}{data['country']}{f}")
        print(f"{amarelo}Código do País: {ciano}{data['countryCode']}{f}")
        print(f"{amarelo}Região: {ciano}{data['region']}{f}")
        print(f"{amarelo}Nome da Região: {ciano}{data['regionName']}{f}")
        print(f"{amarelo}Cidade: {ciano}{data['city']}{f}")
        print(f"{amarelo}Distrito: {ciano}{data['district']}{f}")
        print(f"{amarelo}CEP: {ciano}{data['zip']}{f}")
        print(f"{amarelo}Latitude: {ciano}{data['lat']}{f}")
        print(f"{amarelo}Longitude: {ciano}{data['lon']}{f}")
        print(f"{amarelo}Fuso Horário: {ciano}{data['timezone']}{f}")
        print(f"{amarelo}Offset: {ciano}{data['offset']}{f}")
        print(f"{amarelo}Moeda: {ciano}{data['currency']}{f}")
        print(f"{amarelo}ISP: {ciano}{data['isp']}{f}")
        print(f"{amarelo}Organização: {ciano}{data['org']}{f}")
        print(f"{amarelo}AS: {ciano}{data['as']}{f}")
        print(f"{amarelo}Nome AS: {ciano}{data['asname']}{f}")
        print(f"{amarelo}Reverse DNS: {ciano}{data['reverse']}{f}")
        print(f"{amarelo}É Móvel: {ciano}{data['mobile']}{f}")
        print(f"{amarelo}É Proxy: {ciano}{data['proxy']}{f}")
        print(f"{amarelo}É Hospedagem: {ciano}{data['hosting']}{f}")
    else:
        print(f"{vermelho}Não foi possível obter os dados do IP.{f}")

# Consulta o IP
ip = "24.48.0.1"
dados_ip = consultar_ip(ip)

# Exibe os dados
exibir_dados_ip(dados_ip)

# Pergunta se deseja fazer uma nova consulta
opcao = input("Deseja fazer uma nova consulta? (s/n): ")
if opcao.lower() == "s":
    novo_ip = input("Digite o novo IP: ")
    dados_novo_ip = consultar_ip(novo_ip)
    exibir_dados_ip(dados_novo_ip)
else:
    print("Consulta encerrada.")

