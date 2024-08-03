import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item.get('Company')
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item.get('Item', 'N/A'),
            "price": item.get('price', 'N/A'),
            "description": item.get('description', 'N/A')
        })

else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo= f'{nome_do_restaurante}.json'
    with open (nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)