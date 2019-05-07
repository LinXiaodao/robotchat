#@Author: linjinkun
#@Date: 2019-05-07 10:32:09
#@Last Modified by:   linjinkun
#@Last Modified time: 2019-05-07 10:32:09
 
import socket,threading,time
from server.reply import Robot
class StartServer:
    def __init__(self,addr,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #监听端口
        self.s.bind((addr,port))
        #允许连接最大数量
        self.s.listen(5)
        print('等待连接.....')

        while True:
            # 接受一个新连接:
            sock, addr = self.s.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

    def tcplink(self,sock, addr):
        print('Accept new connection from %s:%s...' % addr)
        robot = Robot()
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            #与机器人聊天
            resonse_word = robot.get_response(data.decode('utf-8'))
            #响应客户端
            sock.send(resonse_word.encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' % addr)



