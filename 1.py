#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#时间结构体

class time_convert():
    def __init__(self):
        self.time = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.min = 0
        self.second = 0

    def input(self):
        # time = input("pls input time")
        flag = True
        timeNum = int(self.time)
        if timeNum < 10000000000000 or timeNum > 99999999999999:
            flag = False
        else:
            self.year = int(self.time[0:4])
            self.month = int(self.time[4:6])
            if self.month < 1 or self.month > 12:
                flag = False
            self.day = int(self.time[6:8])
            if self.month == 2:
                if self.day < 0 or self.day > 29:
                    flag = False
            else:
                if self.day < 0 or self.day > 28:
                    flag = False
            self.hour = int(self.time[8:10])
            if self.hour < 0 or self.hour > 23:
                flag = False
            self.min = int(self.time[10:12])
            if self.min < 0 or self.min > 59:
                flag = False
            self.second = int(self.time[12:])
            if self.second < 0 or self.min > 59:
                flag = False

            if flag == False:
                print("Wrong Time")
            else:
                print(str(self.year) + "-" + str(self.month).zfill(2) + "-" + str(self.day).zfill(2) + " " + str(self.hour).zfill(2) + ":" + str(self.min).zfill(2) + ":" + str(self.second).zfill(2))


t = time_convert()
t.time = input("pls input time")
t.input()