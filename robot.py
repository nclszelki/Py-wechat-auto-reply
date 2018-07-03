import re
import time
import itchat
from itchat.content import *

@itchat.msg_register([TEXT],[PICTURE])
def text_reply(msg):
    reciever = itchat.search_friends(userName=msg['filehelper']) # msg['FromUserName'] is encrypted
    replyContent = "Received your message【%s】" % (msg['Type'])
    if msg['Type'] == 'Text' and re.search(r"auto-reply", msg['Content']):
        replyContent += "Yo! How are you!"
        itchat.send('@img@%s' % 'bebaving-good.jpeg',toUserName=msg['FromUserName'])
    itchat.send("friend:【%s（nickname：%s）】at：【%s】send messages: 【%s】" % (reciever['NickName'], reciever['RemarkName'], time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()), msg['Text']),toUserName='filehelper')
    itchat.send(replyContent,toUserName=msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
