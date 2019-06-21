import win32gui
import win32con
import win32clipboard as w
import base64
from Crypto.Cipher import AES
import urllib.parse
import urllib
import os
import re
name = None
key = None
def setload():
    global key,name
    try:
        f = open('aes密钥文件（此文件为保存的密钥）','r')
        keyname = f.read()
        f.close
        rkey = str(re.findall('.*/', keyname,flags=0))

        key = rkey[2:-3]
        rname = str(re.findall('/.*',keyname,flags=0))
        name= rname[3:-2]
    except :
        pass
        print('cuowu')
# def key_input(key2):
#     global key
#     key = key2

# def name_input(name2):
#     global name
#     name = name2
def load():
    global key,name
    key = (input('输入密钥'))
    name = input('输入聊天窗口名')

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
    
def encrypt_oracle(n):
    # 秘钥
    # key = key2
    # 待加密文本
    n2 = urllib.parse.quote(n)
    text = (n2)
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text
 
#发送的消息
# msg = "测试代码"
#窗口名字
## name = "python code"
# #将测试消息复制到剪切板中
# w.OpenClipboard()
# w.EmptyClipboard()
# w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
# w.CloseClipboard()
#获取窗口句柄



#while 1==1:
def aaaa(msg):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
def send(n):
    setload()
    handle = win32gui.FindWindow(None,name)
    text = str(n)
    msg = encrypt_oracle(text)
    aaaa(msg)
    #填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    #回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    print(name)
if __name__ == "__main__":
    send(input())