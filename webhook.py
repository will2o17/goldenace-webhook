from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_data(as_text=True)

    # 🔍 LOG what TradingView actually sent
    print("INCOMING_FROM_TV:", repr(data))

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": data
    }

    # Send to Telegram & log Telegram’s response
    r = requests.post(url, json=payload)
    print("TELEGRAM_RESPONSE:", r.status_code, r.text)

    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    return "GoldenAce Webhook Running!", 200

if __name__ == "__main__":
    app.run()
