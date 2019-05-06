import socket,threading,time
from reply import Robot

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
#允许连接最大数量
s.listen(5)
print('等待连接.....')

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


