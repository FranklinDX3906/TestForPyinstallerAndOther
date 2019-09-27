#coding:UTF-8

import tkinter as tk
from numpy.distutils.cpuinfo import command_by_line

class HiCBB:
    def __init__(self,root):
        self.frame1 = tk.Frame(root)#创建一个框架
        self.frame2 = tk.Frame(root)


        
    def Test(self):
        def say_hi():
            TextShow.set("你好啊，曹不不")
            next['state'] = 'disabled'
            Quit = tk.Button(self.frame2,text = "退出",fg = "black",command = root.quit)#产生一个新的按钮
            Quit.pack()
                
        self.frame1.pack()#自动调整窗口大小
        self.frame2.pack()
        TextShow = tk.StringVar()#创建一个字段
        TextShow.set("我是DX3906")
        TextLabel = tk.Label(self.frame1, textvariable = TextShow,justify = tk.LEFT,font = 'Helvetica -30 bold')#使用一个label展示字段
        TextLabel.pack(padx=100,pady = 100)
        
        next =  tk.Button(self.frame2, text = "233333", fg="black",command = say_hi)
        next.pack()
        

        

root = tk.Tk()
root.title("测试用")
Test = HiCBB(root)
Test.Test()

root.mainloop()
