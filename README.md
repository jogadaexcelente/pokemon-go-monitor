# 📰 Monitor de Notícias Pokémon GO

Este projeto monitora a página de notícias do Pokémon GO e envia novos posts automaticamente para um canal do Discord por meio de um Webhook.

## 🔧 Como funciona

- A aplicação usa Flask para criar um servidor web.
- A cada acesso à rota `/check`, o script:
  1. Verifica se há novos posts na página oficial de notícias.
  2. Compara com o histórico salvo localmente.
  3. Envia os novos links encontrados para um webhook do Discord.

## 🌐 Demonstração

Servidor ativo em:  
🔗 [https://pokemon-go-monitor.onrender.com](https://pokemon-go-monitor.onrender.com)  
Verificação manual:  
🔍 [https://pokemon-go-monitor.onrender.com/check](https://pokemon-go-monitor.onrender.com/check)

## 🚀 Deploy no Render

1. Crie um repositório no GitHub com o código.
2. No [Render](https://render.com/):
   - Crie um novo "Web Service"
   - Conecte ao seu repositório
   - Configure:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python main.py`
     - Runtime: Python 3
3. O Render detectará automaticamente a porta e iniciará o serviço.

## 🔁 Automação com Cron

Para verificar a rota `/check` a cada hora, use serviços como:

- [cron-job.org](https://cron-job.org/)
- [UptimeRobot](https://uptimerobot.com/)

## 📂 Estrutura do Projeto

