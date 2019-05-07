#@Author: linjinkun
#@Date: 2019-05-07 10:31:31
#@Last Modified by:   linjinkun
#@Last Modified time: 2019-05-07 10:31:31
 
import time


def get_cur_time():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
