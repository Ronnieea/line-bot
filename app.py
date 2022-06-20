from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
    msg = event.message.text
    r = '我看不懂你說什麼'


    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位，是嗎'
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='1',
            sticker_id='1'
    ))

if __name__ == "__main__":
    app.run()