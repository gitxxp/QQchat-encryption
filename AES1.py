import tkinter as tk        #导入tkinter模块
import jiami
import jiema
import os, sys
import _thread
import os
import tkinter.messagebox

window = tk.Tk()            #主窗口
window.title('my window')   #窗口标题
window.geometry('600x400')  #窗口尺寸宽X高
l = tk.Label(window, text='AES聊天消息收发加密解密', bg='green', font=('Arial', 14), width=30, height=2)
l.pack()

l2 = tk.Label(window, text='初次运行务必首先设置密钥及聊天窗口名,按下面按钮，在dos窗输入', bg='red', font=('Arial', 11), width=35, height=2)
l2.pack(fill='x')

_thread.start_new_thread(jiema.run,("开始",'监听剪贴板'))

### 这里是窗口的内容###

def save():
    f = open('aes密钥文件（此文件为保存的密钥）','w')
    f.write(jiami.key+'/'+jiami.name)
    f.close

def hit2():
    jiami.load()
    

def hit_run():
    # global hit
   a= t.get("0.0", "end")
   print(a)
   jiami.send(a)
   return t.get("0.0", "end")
show = '此为端对端加密聊天消息软件\n采用AES对称加密\n你需要与对方先协商好密钥，双方使用相同的密钥即可解密\n注意：请不要把密钥在网络间随意传输，或许你可以通过面对面，邮件传输，信件等方式与对方协定相同的密钥\n使用方法：\n首次运行时：先执行‘重置密钥以及对话窗口名’按钮，退出前可用‘保存设置’保存密钥\n      解密方法：选定密文，Ctrl+C即可显示在DOS窗口中，注意查看\n      加密方法：直接在软件文本框打字发送即可'
def introduce():
    tkinter.messagebox.showinfo('关于',show)

b1 = tk.Button(window, 
    
    text='保存设置',      # 显示按钮上的文字
    width=15, height=2, 
    command=save)     # 点击按钮执行的命令
b1.pack()                # 按钮位置

b2 = tk.Button(window, 
    
    text='重置密钥以及对话窗口名',      # 显示按钮上的文字
    width=20, height=2, 
    command=hit2)     # 点击按钮执行的命令
b2.pack()                # 按钮位置

b3 = tk.Button(window, 
    
    text='介绍及使用说明',      # 显示按钮上的文字
    width=20, height=2, 
    command=introduce)     # 点击按钮执行的命令
b3.pack()                # 按钮位置

c = tk.Button(window, 
    text='发送',      # 显示按钮上的文字
    width=15, height=2, 
    command=hit_run)     # 点击按钮执行的命令
c.pack(side='right')     

t = tk.Text(window, height=3)
t.pack(side='right')


window.mainloop() 
