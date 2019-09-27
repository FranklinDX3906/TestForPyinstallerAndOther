#coding:UTF-8

import tkinter as tk

class HiCBB:
    def __init__(self,root):
        self.frame1 = tk.Frame(root)#创建一个框架
        self.frame2 = tk.Frame(root)


        
    def Test(self):
        def say_hi():
            TextShow.set("你好啊，曹不不")
                
        self.frame1.pack()#自动调整窗口大小
        self.frame2.pack()
        TextShow = tk.StringVar()#创建一个字段
        TextShow.set("我是DX3906")
        TextLabel = tk.Label(self.frame1, textvariable = TextShow,justify = tk.LEFT,font = 'Helvetica -30 bold italic')#使用一个label展示字段
        TextLabel.pack(padx=100,pady = 100)
        
        self.next =  tk.Button(self.frame2, text = "233333", fg="black",command = say_hi)
        self.next.pack()
        

        

root = tk.Tk()
root.title("测试用")
Test = HiCBB(root)
Test.Test()

root.mainloop()

'''        
from tkinter import *

def callback():
    var.set("吹吧你，我才不信嘞！")

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
# 创建一个文本Label对象
var = StringVar()
var.set("您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)
# 创建一个图形Label对象
# 用PhotoImage实例化一个图片对象(支持gif格式文件哦)
# 加一个按钮
theButton = Button(frame2, text="已满18周岁", command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()

'''