import webbrowser
import requests

# Abrir o arquivo HTML no navegador
webbrowser.open('loginkey.html')

# Enviar uma solicitação HTTP para o localhost indicando que está online
localhost_url = 'http://localhost'  # URL padrão do localhost
port = 8000  # Porta do servidor local, ajuste conforme necessário
site_url = f'{localhost_url}:{port}'  # URL completa do servidor local

try:
    response = requests.get(site_url)
    if response.status_code == 200:
        print("O servidor local está online! Link:", site_url)
    else:
        print("O servidor local não está respondendo corretamente.")
except requests.ConnectionError:
    print("Não foi possível conectar ao servidor local.")
