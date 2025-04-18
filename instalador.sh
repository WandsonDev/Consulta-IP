#!/bin/bash
termux-setup-storage
clear
# Define as cores
amarelo='\033[1;33m'
ciano='\033[1;36m'
reset='\033[0m'


echo -e "${amarelo}[ ! ] ANTES DE BAIXAR AS DEPENDÊNCIAS NECESSÁRIAS, PRECISO DA SUA PERMISSÃO PARA INSTALAR AS COISAS NECESSÁRIAS PARA ESTE SCRIPT FUNCIONAR PERFEITAMENTE.${reset}"


echo -e "${ciano}[ ? ] Permite a Instalação? Digite \"y\" Para Sim e \"n\" para Não. (y/n)"
read resposta


if [[ $resposta == "y" || $resposta == "Y" ]]; then
    echo -e "${ciano}[ ! ] Tenha Paciência, Pode Demorar Variando da Sua Internet e do Servidor${reset}"
    echo 
    echo -e "${amarelo}[ ! ] INSTALANDO DEPENDÊNCIAS, AGUARDE... (0%)${reset}"
    pkg install git -y > /dev/null 2>&1
    echo 
    echo -e "${amarelo}[ ! ] INSTALANDO DEPENDÊNCIAS, AGUARDE... (25%)${reset}"
    pkg install python3 -y > /dev/null 2>&1
    echo 
    echo -e "${amarelo}[ ! ] INSTALANDO DEPENDÊNCIAS, AGUARDE... (50%)${reset}"
    pkg install nano -y > /dev/null 2>&1
    echo 
    echo -e "${amarelo}[ ! ] INSTALANDO DEPENDÊNCIAS, AGUARDE... (75%)${reset}"
    pip install requests > /dev/null
    echo 
    echo -e "${amarelo}[ ! ] INSTALANDO DEPENDÊNCIAS, AGUARDE... (99%)${reset}"
    pip install termcolor > /dev/null
    echo 
    echo 
    echo -e "${amarelo}[ ✔️ ] DEPENDÊNCIAS INSTALADAS, DE python3 start.py PARA CONTINUAR. ${reset}"
    echo 
elif [[ $resposta == "n" || $resposta == "N" ]]; then
    echo -e "${amarelo}Instalação cancelada.${reset}"
else
    echo -e "${amarelo}Resposta inválida. Saindo...${reset}"
fi
