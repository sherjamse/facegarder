from flask import Flask , request , abort
from linebot import(LineBotApi,WebhookHandler)
from linebot.exception import (InvalidSignarteError)
from linebot.models import *

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('rWGdxD8wrVJOO76lTy9O9uIAZT/6HJ3YbV224h2YB7W6o+pC0pAFXMiINUB3CdCr0R+VDtakzaj3PavZFIeuz37YbHjyDTDfzkRa5vjLdzmmzj/a26i9rSGIxTJXKBb9NuY+OCIJ8p8yMiyq4lvqVwdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('82f9b5062c38d4ed0c6b5b67c276d378')
line_bot_api.push_message('U98ac08c5a53b49644b1a5d0d0808ec5a', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
 
    return 'OK'
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
    #主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)