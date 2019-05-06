import socket

class CreateSocket:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        self.s.connect(('127.0.0.1', 9999))
    
    def send_msg_server(self,data):
        self.s.send(data.encode())
        # respon_now = get_cur_time() +'\n' + '机器人：'
        return self.s.recv(1024).decode('utf-8')
# 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# while True:
#     data = input("请输入：")
#     s.send(data.encode())
#     if data == 'exit':
#         break
#     print(s.recv(1024).decode('utf-8'))

