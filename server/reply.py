#@Author: linjinkun
#@Date: 2019-05-07 10:32:23
#@Last Modified by:   linjinkun
#@Last Modified time: 2019-05-07 10:32:23
 
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