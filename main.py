from flask import Flask
import requests
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)

URL = "https://pokemongo.com/news?hl=pt_BR"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/707303045431558154/SlIvgVldgTE4LPKxmY50VPB983WW58S3lEbWevKGSMhecMhALPrz599gD7_HNDdi_ymN"
HISTORY_FILE = "post_history.json"


def load_history():
    if not os.path.isfile(HISTORY_FILE):
        return set()
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(list(history), f)


def fetch_latest_posts():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (compatible; DiscordBot/2.0; +https://discordapp.com)"
    }
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("a.blogList__post")
    posts = []
    for post in post_links:
        href = post.get("href")
        if href:
            full_url = "https://pokemongo.com" + href
            posts.append(full_url)
    return posts


def send_to_discord(posts):
    for post_url in posts:
        data = {"content": f"🆕 Novo post no Pokémon GO News:\n{post_url}"}
        try:
            requests.post(DISCORD_WEBHOOK, json=data)
        except Exception as e:
            print(f"Erro ao enviar para Discord: {e}")


@app.route("/")
def home():
    return "Monitor de notícias Pokémon GO ativo! 🚀"


@app.route("/check")
def check_new_posts():
    history = load_history()
    current_posts = fetch_latest_posts()
    new_posts = [p for p in current_posts if p not in history]

    if new_posts:
        print(f"🆕 {len(new_posts)} novos posts enviados ao Discord!")
        send_to_discord(new_posts)
        history.update(new_posts)
        save_history(history)
        return f"{len(new_posts)} novos posts enviados ao Discord!"
    else:
        print("✅ Nenhum post novo encontrado.")
        return "Nenhum post novo encontrado."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
