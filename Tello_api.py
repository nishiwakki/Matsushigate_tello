# [INFOMATION]
# Tello_api.py
# define some functions related to Tello.
# nishiwaki : 2022/01/15
# 
# [PREFERENCE]
# OpenCV: VideoCapture Class Reference
# https://docs.opencv.org/4.5.3/d8/dfe/classcv_1_1VideoCapture.html
# OpenCV: High-level GUI
# https://docs.opencv.org/4.5.3/d7/dfc/group__highgui.html

# -*- coding: utf-8 -*-

import socket
import cv2
from datetime import datetime
from time import sleep, strftime
from math import ceil

class Drone():
    #---------------------------------------
    # Class Constants
    #---------------------------------------

    # Tello
    IP_TELLO = '192.168.10.1'
    PT_TELLO = 8889
    __AD_TELLO = (IP_TELLO, PT_TELLO)
    # VideoStream receiver
    IP_VS_RECV = '0.0.0.0' # '127.0.0.1'
    PT_VS_RECV = 11111
    # Other
    PATH = 'pictures/'
    FORMAT = '%Y%m%d_%H%M%S.jpg'

    #---------------------------------------
    # Constructor
    #---------------------------------------

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.command()

    #---------------------------------------
    # Public Methods
    #---------------------------------------

    # 
    # COMMON COMMANDS
    #

    # Send command to Tello
    def send(self, comm):
        self.sock.sendto(comm.encode('utf-8'), Drone.__AD_TELLO)

    # wait x[secs]
    def wait(self, sec=5):
        sleep(sec)

    # 
    # CONTROL COMMANDS
    # 

    # Enter SDK mode
    def command(self):
        self.send('command')

    # Auto takeoff
    def takeoff(self):
        self.send('takeoff')
        self.wait(10)

    # Auto landing
    def land(self):
        self.send('land')

    # Enable video stream
    def streamon(self):
        self.send('streamon')
    
    # Disable video stream
    def streamoff(self):
        self.send('streamoff')

    # Ascend to x[cm] (20≤x≤500)
    def up(self, x=100):
        self.send('up ' + str(x))
        self.wait(ceil(x/75)+1)

    # Descend to x[cm] (20≤x≤500)
    def down(self, x=100):
        self.send('down ' + str(x))
        self.wait(ceil(x/75)+1)

    # Fly left for x[cm] (20≤x≤500)
    def left(self, x=100):
        self.send('left ' + str(x))
        self.wait(ceil(x/75)+1)

    # Fly right for x[cm] (20≤x≤500)
    def right(self, x=100):
        self.send('right ' + str(x))
        self.wait(ceil(x/75)+1)

    # Fly forward for x[cm] (20≤x≤500)
    def forward(self, x=100):
        self.send('forward ' + str(x))
        self.wait(ceil(x/75)+1)

    # Fly back for x[cm] (20≤x≤500)
    def back(self, x=100):
        self.send('back ' + str(x))
        self.wait(ceil(x/75)+1)
    
    # Rotate x[degrees] clockwise (1≤x≤360)
    def rotate(self, x=180, y='R'):
        if y == 'L' or y == 'l':
            self.send('ccw ' + str(x))
        else:
            self.send('cw ' +  str(x))
        self.wait(ceil(x/50)+1)
    
    # 
    # OPTIONAL COMMAND
    # 

    # Take a picture
    def picture(self):
        filename = Drone.PATH + \
                        datetime.now().strftime(Drone.FORMAT)
        self.streamon()
        cap = cv2.VideoCapture('udp://' + Drone.IP_VS_RECV + \
                                    ':' + str(Drone.PT_VS_RECV))
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(filename, frame)
                break
        cap.release()
        self.streamoff()
