
import base64
from Crypto.Cipher import AES
import pyperclip
import tkinter.messagebox
import tkinter as tk 
import time 
import urllib.parse
import urllib
import os
import re
'''
采用AES对称加密算法
'''

 

# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

#解密方法
def setload():
    global key,name
    try:
        f = open('aes密钥文件（此文件为保存的密钥）','r')
        keyname = f.read()
        f.close
        rkey = str(re.findall('.*/', keyname,flags=0))
        key = rkey[2:-3]
    except :
        pass
        print('cuowu')

def decrypt_oralce(n):
     try:
                    #      秘钥
         
          
          # 密文
          text = n
          # 初始化加密器
          aes = AES.new(add_to_16(key), AES.MODE_ECB)
          #优先逆向解密base64成bytes
          base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
          #执行解密密并转码返回str
          decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','') 
          return urllib.parse.unquote(decrypted_text)
     except:
          print('目前仅支持复制密文')

def cut():
     return str(pyperclip.paste())

def run(a,b):
     last_cut = 'CzAVrz6SeanMiV0V8dKI/t2fwi5Cb/OIClHmjPgmy8Bfoh5seCP/mmcH2plZke057aCG+VqDk7lFQtcEqvq0QmfKkpey/xQA1T56sjOC8Pk='
     setload()
     print(a,b)
     print('解密方法：选定密文，Ctrl+C即可')
     while True:
          time.sleep(1)
          
          if cut() != last_cut:
               n = cut()
               # tkinter.messagebox.showwarning('明文',decrypt_oralce(n))
               print('明文：',decrypt_oralce(n))
               # print(('明文',decrypt_oralce(n)))
               last_cut = cut()
          

if __name__ == "__main__":
    run('1','2')    
      
        
