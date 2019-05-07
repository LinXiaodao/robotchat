# # -*- coding:utf-8 -*-

# import socket
# import urllib
# import json
# import sys
# # reload(sys)
# # sys.setdefaultencoding('utf-8')

# #info = 'python'
# def get_computer(info):
#     key = '186cccedc79549ecac4dcc8a56fc9fb4'
#     api = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
#     response =urllib.urlopen(api).read()
#     dic_json = json.loads(response)
#     return '机器人:'.decode('utf-8')+dic_json['text']
# host = socket.gethostbyname(socket.gethostname())
# print(host)
# port =11112
# s = socket.socket()
# s.bind((host,port))
# s.listen(1)

# while True:
#     clnt,addr = s.accept()
#     print('client address:',addr)
#     while True:
#         data = clnt.recv(1024)
#         #print data
#         if not data:sys.exit()
#         print('going to :',data)
#         result = get_computer(data)
#         if len(result) == 0:
#             result = "EXD"
#         clnt.sendall(result)

# clnt.close()


import requests
from common.date import get_cur_time
class Robot:
    def __init__(self):
        self.KEY = '6244875a21b14000b1f350f9145e41f1'
 
    def get_response(self,msg):
        apiUrl = 'http://www.tuling123.com/openapi/api'
        data = {
            'key'    : self.KEY,
            'info'   : msg,
        }
        try:
            r = requests.post(apiUrl, data=data).json()
            respon_now = get_cur_time() +'\n' + '机器人：'
            return respon_now + r.get('text')
        except:
            return '机器人挂了'
# print(get_response('你好'))