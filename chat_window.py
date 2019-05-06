from tkinter import *
from pynput.keyboard import Key,Controller,Listener
class CreateWindow:
    def create_window(self):
        #创建窗口
        t = Tk()
        t.title('聊天中....')

        #创建frame容器
        frmLT = Frame(width=500, height=320, bg='white')
        frmLC = Frame(width=500, height=150, bg='white')
        frmLB = Frame(width=500, height=30)

        #发送取消按钮和图片
        btnSend = Button(frmLB, text='发 送', width = 8, command=self.sendMsg)
        btnCancel = Button(frmLB, text='取消', width = 8, command=self.cancelMsg)
        #按钮和图片
        btnSend.grid(row=2,column=0)
        btnCancel.grid(row=2,column=1)

        #而rowspan选项同样可以指定控件跨越多行显示。
        frmLT.grid(row=0, column=0,columnspan=2, padx=1, pady=3)
        frmLC.grid(row=1, column=0, columnspan=2,padx=1, pady=3)
        frmLB.grid(row=2, column=0, columnspan=2,padx=1, pady=3)


        #固定大小
        frmLT.grid_propagate(0)
        frmLC.grid_propagate(0)
        frmLB.grid_propagate(0)


        #创建控件
        self.getMsgBox = Text(frmLC)
        self.showMsg = Text(frmLT)
        self.getMsgBox.grid()
        self.showMsg.grid()

        #监听键盘
        # self.getMsgBox.bind('<Key>',self.getKey)
        # self.getKey()

        #主事件循环
        t.mainloop()

    def sendMsg(self):
        '''发送消息'''
        #消息内容
        sendWord = self.getMsgBox.get('0.0', END)
        #显示到对话列表
        self.showMsg.insert(END,sendWord)
        #清空输入框
        self.cancelMsg()

    def cancelMsg(self):
        '''清除输入框'''
        self.getMsgBox.delete('0.0', END)

    # def getKey(self):
    #     def on_press(key):
    #         print(key,'建明')
    #     with Listener(on_press=on_press) as listener:
    #         listener.join()
cw = CreateWindow()
cw.create_window()