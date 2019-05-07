import time


def get_cur_time():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
