![Banner](https://cdn.discordapp.com/attachments/1424141770245275760/1475548098162983186/Bannergithub.png?ex=699de2c0&is=699c9140&hm=f723514c8ef3b2321c2222459ba6e75140646124c0a577136d30feae7c517429&)
# 🏛️ Bot de Tasas BCV - Comunidad Rimk Coffee
![Banner2](https://cdn.discordapp.com/attachments/1424141770245275760/1475549749422592312/Bannergithub2.png?ex=699de44a&is=699c92ca&hm=e7cc4c993b94bac33012c346a17e2d67740ddaee0f8c18072af8a7e5c5d9309d&)
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
