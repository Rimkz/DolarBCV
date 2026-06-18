import requests
from bs4 import BeautifulSoup
import os
import re
import urllib3

# Silencia la publicidad molesta en la terminal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CONFIGURACIÓN DE SERVIDORES
SERVIDORES = [
    {
        "url": os.getenv('DISCORD_WEBHOOK'),
        "color": 14614410
    }
]

URL_BCV = "https://www.bcv.org.ve/"

def limpiar_y_formato(texto):
    try:
        solo_numeros = re.sub(r'[^0-9,.]', '', texto)
        if ',' in solo_numeros and '.' in solo_numeros:
            solo_numeros = solo_numeros.replace('.', '')
        valor_punto = solo_numeros.replace(',', '.')
        valor_final = float(valor_punto)
        return "{:,.2f}".format(valor_final).replace('.', 'X').replace(',', '.').replace('X', ',')
    except:
        return texto

def obtener_tasas():
    try:
        encabezados = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        respuesta = requests.get(URL_BCV, headers=encabezados, verify=False)
        sopa = BeautifulSoup(respuesta.content, 'html.parser')

        d_raw = sopa.find(id="dolar").get_text()
        e_raw = sopa.find(id="euro").get_text()
        fecha = sopa.find(class_="fecha-display-single").get_text().strip()

        dolar = limpiar_y_formato(d_raw)
        euro = limpiar_y_formato(e_raw)

        for servidor in SERVIDORES:
            if servidor["url"]:
                enviar_a_discord(servidor["url"], servidor["color"], dolar, euro, fecha)
                
    except Exception as e:
        print(f"Error general: {e}")

def enviar_a_discord(url, color, dolar, euro, fecha):
    carga_util = {
        "embeds": [{
            "title": "🏛️ BCV | Tasa de Cambio Oficial",
            "description": f"📅 **Fecha:** {fecha}\n",
            "color": color,
            "fields": [
                {
                    "name": "**💵 Dólar (USD)**",
                    "value": "**```diff\n+ " + dolar + " Bs.\n```**", 
                    "inline": True
                },
                {
                    "name": "**💶 Euro (EUR)**",
                    "value": "**```yaml\n" + euro + " Bs.\n```**", 
                    "inline": True
                }
            ],
            "image": {"url": "https://cdn.discordapp.com/attachments/1424141770245275760/1516957133751582810/DolarBCVpng.png?ex=6a3487ec&is=6a33366c&hm=8a11fb5d37b764d3b89a60df797721d6a0adc9fc2b30ed55e6f13d4a00d9dd34&"}, # imagen del banner
            "footer": {
                "text": "bcv.org.ve",
                "icon_url": "https://cdn.discordapp.com/attachments/1424141770245275760/1516958980088397914/SiluetaLogonegro.png?ex=6a3489a4&is=6a333824&hm=e820737f3cc6aa5c36f25eadd81f401dc908c958f7678ec37e2d3f44a8238391&"}
        }]
    }
    requests.post(url, json=carga_util)

if __name__ == "__main__":
    obtener_tasas()
