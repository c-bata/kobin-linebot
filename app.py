import os
from kobin import Kobin, request, Response
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, JoinEvent, TextMessage, TextSendMessage
)

app = Kobin()
line_bot_api = LineBotApi(os.getenv('LINE_BOT_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_BOT_CHANNEL_ACCESS_SECRET'))


@app.route('/')
def index():
    return Response('pong')


@app.route("/callback", method='POST')
def callback():
    signature = request.headers['X_LINE_SIGNATURE']
    print('signature: ', signature)

    # get request body as text
    body = request.body
    print('body: ', body)
    handler.handle(body, signature)

    return Response('OK')


@handler.add(JoinEvent)
def handle_join(event):
    msg = 'Joined this {}!\nみなさん、よろしくお願いします :)'.format(event.source.type)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(msg))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(event.reply_token, messages=TextSendMessage(msg))
