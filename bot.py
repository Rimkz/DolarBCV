solicitudes importantes
desde bs4 importar Hermosa sopa
importar os
importar re
importar urllib3

# Silencia la publicidad molesta en la terminal
urllib3.deshabilitar_advertencias(urllib3.excepciones.Advertencia de solicititud insegura)

# CONFIGURACIÓN DE SERVIDORES
SERVIDORES = [
    {
        "url": os.getenv ('DISCORD_WEBHOOK'),
        "color": 14614410
    }
]

URL_BCV = "https://www.bcv.org.ve/"

def formato limpiar_y_(texto):
    intentar:
        solo_numeros = re.sub(r'[^0-9,.]', '', texto)
        si ',' en solo_numeros y '.' en solo_numeros:
            solo_numeros = solo_numeros.reemplazar('.', '')
        valor_punto = solo_numeros.reemplazar(',', '.')
        valor_final = float(valor_punto)
        retorno "{:,.2f}".formato(valor_final).reemplazar('.', 'X').reemplazar(',', '.').reemplazar('X', ',')
    excepto:
        retorno texto

def obtener_tasas():
    intentar:
        encabezados = {'Agente de usuario': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/119.0.0.0 Safari/537.36'}
        respuesta = solicitudes.get(URL_BCV, encabezados=encabezados, verificar=Falso)
        sopa = Hermosa sopa(respuesta.contenido, 'html.parser')

        d_raw = sopa.encontrar(id="dolar").obtener_texto()
        e_raw = sopa.encontrar(id="euro").obtener_texto()
        fecha = sopa.encontrar(clase_="fecha-display-single").obtener_texto().tira()

        dolar = formato limpiar_y_(d_raw)
        euro = formato limpiar_y_(e_raw)

        para servir en SERVIDORES:
            si servidor["url"]:
                enviar_a_discord(servidor["url"], servidor["color"], dolar, euro, fecha)
                
    excepto Excelencia como e:
        imprimir(f"Error general: {e}")

def enviar_a_discord(url, color, dolar, euro, fecha):
    carga útil = {
        "incrustaciones": [{
            "típulo": "🏛️ BCV | Tasa de Cambio Oficial",
            "descripción": f"📅 **Fecha:** {fecha}\n",
            "color": color,
            "campos": [
                {
                    "nombre": "**💵 Dólar (USD)**",
                    "valor": "**```diff\n+ " + dolar + " Bs.\n```**", 
                    "en línea": Verdadero
                },
                {
                    "nombre": "**💶 Euro (EUR)**",
                    "valor": "**```yaml\n" + euro + "Bs.\n```**", 
                    "en línea": Verdadero
                }
            ],
            "imagen": {"url": "https://cdn.discordapp.com/attachments/1424141770245275760/1516957133751582810/DolarBCVpng.png?ex=6a3487ec&is=6a33366c&hm=8a11fb5d37b764d3b89a60df797721d6a0adc9fc2b30ed55e6f13d4a00d9dd34&"}, # imagen del banner
            "pie de página": {
                "texto": "bcv.org.ve",
                "icon_url": "https://cdn.discordapp.com/attachments/1424141770245275760/1516958980088397914/SiluetaLogonegro.png?ex=6a3489a4&is=6a333824&hm=e820737f3cc6aa5c36f25eadd81f401dc908c958f7678ec37e2d3f44a8238391&"}
        }]
    }
    solicitudes.post(url, json=carga útil)

si __nombre__ == "__principal__":
    obtener_tasas()
