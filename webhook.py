from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    # Get raw body from TradingView / ReqBin
    data = request.get_data(as_text=True)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": data,
        "parse_mode": "HTML"
    }

    # Send to Telegram
    r = requests.post(url, json=payload)

    # 🔥 LOG TELEGRAM'S REPLY
    print("TELEGRAM RESPONSE:", r.status_code, r.text)

    return "OK", 200


@app.route("/", methods=["GET"])
def home():
    return "GoldenAce Webhook Running!", 200


if __name__ == "__main__":
    app.run()
