import time as t
import os
import win32api, win32con
import datetime

from win32gui import SetWindowPos

try:
    reg = "/\s+/"
    date = list()
    time = list()
    thing = list()
    round = list()

    ctime = os.path.getmtime("dailyList.txt")


    def q():
        file = open("dailyList.txt", "r", encoding="utf-8")
        date.clear()
        time.clear()
        thing.clear()
        round.clear()
        while 1:

            line = file.readline()
            if not line:
                break
            date1 = line.split()[0]
            time1 = line.split()[1]
            thing1 = line.split()[2]
            round1 = line.split()[3]
            # print(date1, time1, thing1, round1)
            date.append(date1)
            time.append(time1)
            thing.append(thing1)
            round.append(round1)
        file.close()
        # print(date, time, thing, round)


    q()
    while 1:

        t.sleep(1)
        if ctime != os.path.getmtime("dailyList.txt"):
            q()
            ctime = os.path.getmtime("dailyList.txt")
        # 获取当前系统时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ndate = now.split()[0]
        ny = ndate.split("-")[0]
        nm = ndate.split("-")[1]
        nd = ndate.split("-")[2]
        ntime = now.split()[1]

        if ntime in time:
            index = time.index(ntime)
            dd = date[index].split("-")
            y = dd[0]
            m = dd[1]
            d = dd[2]

            if round[index] == "每日":
                win32api.MessageBox(0, thing[index], "Ao提醒", win32con.MB_OK)
            if round[index] == "每月":
                if nd == d:
                    win32api.MessageBox(0, thing[index], "Ao提醒", win32con.MB_OK)
            if round[index] == "每年":
                if nm == m:
                    if nd == d:
                        win32api.MessageBox(0, thing[index], "Ao提醒", win32con.MB_OK)
except:
    win32api.MessageBox(0, "程序异常!请重启程序或联系作者", "Ao提醒", win32con.MB_OK)