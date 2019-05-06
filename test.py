# from tkinter import *

# root=Tk()        
# root.title('QQ聊天窗口')     #title
# root.geometry('320x240')

# # li  = ['C','python','php','html','SQL','java']
# listb = Listbox(root)
# # for item in li:                 # 第一个小部件插入数据
# #     listb.insert(0,item)
# # listb.pack()


# while True:
#     data = input("请输入：")
#     if data == 'exit':
#         break
#     listb.insert(0,data)
#     listb.pack()
# root.mainloop()

import os
from tkinter import *
import time

# os.chdir('E:\\actdata')
 
def main():
 
  def sendMsg():#发送消息
    strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                  time.localtime()) + '\n '
    print(strMsg)
    txtMsgList.insert(END, strMsg,"greencolor")#插入年月日
    txtMsgList.insert(END, txtMsg.get('0.0', END))#输入的内容,0.0表示文本开始
    txtMsg.delete('0.0', END)#删除中间刚输入的内容
     
  def cancelMsg():#取消消息
    txtMsg.delete('0.0', END)
 
  def sendMsgEvent(event): #发送消息事件:
    if event.keysym == "Enter":
      sendMsg()
 
  #创建窗口 
  t = Tk()
  t.title('与Python聊天中')
       
  #创建frame容器
  frmLT = Frame(width=500, height=320, bg='white')
  frmLC = Frame(width=500, height=150, bg='white')
  frmLB = Frame(width=500, height=30)
  frmRT = Frame(width=200, height=500)
   
  #创建控件
  txtMsgList = Text(frmLT)
 # txtMsgList.tag_config('greencolor', foreground='#008C00')#创建tag
  txtMsg = Text(frmLC);
  txtMsg.bind("<KeyPress-Up>", sendMsgEvent)

  #发送取消按钮和图片
  btnSend = Button(frmLB, text='发 送', width = 8, command=sendMsg)
  btnCancel = Button(frmLB, text='取消', width = 8, command=cancelMsg)
  imgInfo = PhotoImage(file = "C:\\Users\\linji\\Pictures\\l.png")
  lblImage = Label(frmRT, image = imgInfo)
  lblImage.image = imgInfo
 
  #窗口布局columnspan选项可以指定控件跨越多列显示，
  #而rowspan选项同样可以指定控件跨越多行显示。
  frmLT.grid(row=0, column=0,columnspan=2, padx=1, pady=3)
  frmLC.grid(row=1, column=0, columnspan=2,padx=1, pady=3)
  frmLB.grid(row=2, column=0,columnspan=2)
  frmRT.grid(row=0, column=2, columnspan=2,rowspan=3, padx=2, pady=3)
  #固定大小
  frmLT.grid_propagate(0)
  frmLC.grid_propagate(0)
  frmLB.grid_propagate(0)
  frmRT.grid_propagate(0)

   #按钮和图片
  btnSend.grid(row=2,column=0)
  btnCancel.grid(row=2,column=1)
  lblImage.grid()
  
  txtMsgList.grid()
  txtMsg.grid()
 
  #主事件循环
  t.mainloop()
 
if __name__ == '__main__':
    main()