import select
from ctypes import *
import struct, array
from fcntl import ioctl
from sys import argv
import getopt
import os
import v4l2capture
import cv2
import numpy as np
import time

lib_path = path + "/lib" + "/libart_driver.so"
so = cdll.LoadLibrary
lib = so(lib_path)
car = "/dev/ttyACM0"
offsetThre = 0.4

if (lib.art_racecar_init(38400, car.encode("utf-8")) < 0):
    raise
    pass
try:
    while 1:
        val = 1000
        privity = 1
        if privity == 1:
            #如果偏移量是小于某个值，则看行车规划，如果大于某个值，则速度降低 添加get 获取
            if offset < offsetThre:
                privity = 0
            else:
                val = 500
                angle = 1500 + offset * 10
                lib.send_cmd(val, angle)
                print("angle: %d, throttle: %d" % (a, vel))
        if privity == 0:
            val = 1000
            decision()
            if getEnd() == True:
                break
except:
    print('error')
finally:
    lib.send_cmd(0, 1500)