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

def consultar_ip(ip):
    url = f"https://geo.ipify.org/api/v2/country?apiKey=at_kaqa78aBBe845GUn0eA5tDh3NJ9ug&ipAddress={ip}"
    response = get(url)
    data = loads(response.text)
    return data

def exibir_dados_ip(data):
    print(f"{amarelo}Dados do IP consultado:")
    print(f"{amarelo}IP: {ciano}{data['ip']}{f}")
    sleep(0.8)
    print(f"{amarelo}Localização:")
    print(f"{amarelo}País: {ciano}{data['location']['country']}{f}")
    sleep(0.8)
    print(f"{amarelo}Região: {ciano}{data['location']['region']}{f}")
    sleep(0.8)
    print(f"{amarelo}Fuso Horário: {ciano}{data['location']['timezone']}{f}")
    sleep(0.8)
    print(f"{amarelo}Domínios: {ciano}{', '.join(data['domains'])}{f}")
    sleep(0.8)
    print(f"{amarelo}ASN: {ciano}{data['as']['asn']}{f}")
    sleep(0.8)
    print(f"{amarelo}Nome ASN: {ciano}{data['as']['name']}{f}")
    sleep(0.8)
    print(f"{amarelo}Rota ASN: {ciano}{data['as']['route']}{f}")
    sleep(0.8)
    print(f"{amarelo}Domínio ASN: {ciano}{data['as']['domain']}{f}")
    sleep(0.8)
    print(f"{amarelo}Tipo ASN: {ciano}{data['as']['type']}{f}")
    sleep(0.8)
    print(f"{amarelo}ISP: {ciano}{data['isp']}{f}")
    sleep(0.8)

while True:
    ip = input("Digite o IP que deseja consultar: ")
    data = consultar_ip(ip)
    exibir_dados_ip(data)

    continuar = input("Deseja fazer outra consulta? (s/n): ")
    if continuar.lower() == "s":
        break
    else:
        os.system("python3 src/menu/main.py")
