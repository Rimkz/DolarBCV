![Banner](https://cdn.discordapp.com/attachments/1424141770245275760/1475547335915208745/Bannergithub.png?ex=699de20b&is=699c908b&hm=a0c83caf28edba21b4589a9910787cd1ff282302a169ed91a9515610496965a4&)
# 🏛️ Bot de Tasas BCV - Comunidad Rimk Coffee
Este proyecto nació de la colaboración para automatizar la información financiera del Banco Central de Venezuela de forma elegante y precisa. Originalmente iniciado por [Marco](https://github.com/Marco202024/bcv-discord-bot) y adaptado por [Rimk](https://www.instagram.com/rimk_ve/) con toques finales para la comunidad de Rimk Coffee.

## ✨ Características Principales
* **Precisión Financiera:** Formateo estricto con separadores de miles y 2 decimales según el estándar contable.

* **Ejecución en la Nube:** Automatizado mediante GitHub Actions para funcionar 24/7 sin depender de una PC encendida.

* **Seguridad:** La URL del Webhooks está protegida mediante GitHub Secrets, manteniéndola invisible para terceros.

## 🛠️ Cómo funciona el motor
1. Extracción: El script visita la web oficial del BCV mediante `BeautifulSoup4` y `urllib3`.

2. Procesamiento: Se limpian los datos brutos y se transforman en valores numéricos limpios.

3. Publicación: Se construye un objeto JSON estructurado que se envía a Discord, creando una interfaz visual atractiva para los usuarios.

## 📅 Cronograma de Publicación
El bot está configurado para despertar de martes a viernes a las 5:45 AM (GMT-4), garantizando que la comunidad comience el día con la tasa valor vigente.

---
![Seguridad](https://img.shields.io/github/actions/workflow/status/Marco202024/bcv-discord-bot/main.yml?label=Seguridad&style=for-the-badge)
