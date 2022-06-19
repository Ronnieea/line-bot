from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('T2HB61i3E645KRzMtnT1PO/ncYbv7rOVqGgNCUk+jz4ZotlZj4lmSeVWTY2MfEIX4Qr6R5H2gqz+k8VFdIf5xpSC0LM2OjdZsRbHCOHB0FPXxSBj2dUofphMVMbsHGgUp2ff4J9PUWk50EldT9JhPQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a6867fa09860c49494e82641815671ee')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()