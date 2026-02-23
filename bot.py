import requests
from bs4 import BeautifulSoup
import os
import re
import urllib3

# Silencia la advertencia molesta en la terminal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CONFIGURACIÓN DE SERVIDORES
SERVIDORES = [
    {
        "url": os.getenv ('DISCORD_WEBHOOK'),
        "color": 14614410
    }
]

URL_BCV = "https://www.bcv.org.ve/"

def limpiar_y_formatear(texto):
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
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        response = requests.get(URL_BCV, headers=headers, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        d_raw = soup.find(id="dolar").get_text()
        e_raw = soup.find(id="euro").get_text()
        fecha = soup.find(class_="date-display-single").get_text().strip()

        dolar = limpiar_y_formatear(d_raw)
        euro = limpiar_y_formatear(e_raw)

        for server in SERVIDORES:
            if server["url"]:
                enviar_a_discord(server["url"], server["color"], dolar, euro, fecha)
                
    except Exception as e:
        print(f"Error general: {e}")

def enviar_a_discord(url, color, dolar, euro, fecha):
    payload = {
        "embeds": [{
            "title": "🏛️ BCV | Tasa de Cambio Oficial",
            "description": f"📅 **Fecha:** {fecha}\n",
            "color": color,
            "fields": [
                {
                    "name": "💵 Dólar (USD)",
                    "value": "**```diff\n+ " + dolar + " Bs.\n```**", 
                    "inline": True
                },
                {
                    "name": "💶 Euro (EUR)",
                    "value": "**```yaml\n" + euro + " Bs.\n```**", 
                    "inline": True
                }
            ],
            "image": {"url": "https://cdn.discordapp.com/attachments/1424141770245275760/1475530835791970448/Banner.png?ex=699dd2ad&is=699c812d&hm=c9753688d693e49aa1fa6bc1a98dd75767adb70f1e50cfa22c6eea36040e7da8&"}, # imagen del banner
            "footer": {
                "text": "bcv.org.ve",
                "icon_url": "https://cdn.discordapp.com/attachments/1424141770245275760/1475524862930976838/banco-central-de-venezuela.png?ex=699dcd1d&is=699c7b9d&hm=38cd35b7e8f7e0deca3fa3f615d093a05c592f61942cb970a58c79f60c0b54a6&"}
        }]
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    obtener_tasas()