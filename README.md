---

# Consulta-IP

Projeto simples em Python para obter informações detalhadas de um IP utilizando diversas APIs gratuitas. Adaptado para uso no Termux, mas compatível com qualquer terminal que tenha o Python instalado (Linux, Windows, macOS).

**Atenção:** Todas as informações retornadas são provenientes das APIs utilizadas. O projeto apenas exibe os dados, não tendo vínculo com os provedores das APIs.

---

## Como instalar?

### 1. Instale o Termux (caso esteja em um dispositivo Android)

Baixe pelo F-Droid:  
[https://f-droid.org/pt_BR/packages/com.termux/](https://f-droid.org/pt_BR/packages/com.termux/)

### 2. Clone o repositório

Abra o Termux e execute:

```bash
termux-setup-storage         # Concede permissões ao Termux
pkg install git              # Instala o Git
git clone https://github.com/WandsonDev/Consulta-IP/
```

### 3. Instale as dependências

Execute o script de instalação:

```bash
cd Consulta-IP
bash instalador.sh
```

---

## Como usar?

Dentro da pasta do projeto, execute:

```bash
python3 main.py
```

Um painel no terminal será aberto. Basta escolher a API de consulta e inserir o IP desejado. Pronto.

---

## APIs utilizadas

- [ip-api.com](https://ip-api.com/)
- [ip-tracker.org](https://www.ip-tracker.org/)
- [ipwho.is](https://ipwho.is/)
- [geo.ipify.org](https://geo.ipify.org/)

---

## Dependências

**Pacotes do sistema (via pkg):**  
- `git`
- `python3`

**Pacotes Python (via pip):**  
- `requests`  
- `termcolor`

---
