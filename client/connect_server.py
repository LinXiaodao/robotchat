#@Author: linjinkun
#@Date: 2019-05-07 10:30:54
#@Last Modified by:   linjinkun
#@Last Modified time: 2019-05-07 10:30:54
import socket

class CreateSocket:
    '''连接服务器端口'''
    def __init__(self,addr,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        self.s.connect((addr, port))
    
    def send_msg_server(self,data):
        ''' 与机器人交流
            Args:
                data    发送的消息
            Retrun:
                回答
        '''
        self.s.send(data.encode())
        return self.s.recv(1024).decode('utf-8')
