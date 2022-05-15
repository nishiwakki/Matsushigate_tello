# [INFOMATION]
# Tello_api.py
# define some functions related to Tello.
# nishiwaki : 2022/05/15
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
        self.speed = 100
        self.angle = 180
        self.dist = 100
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
        self.wait(1)

    # Auto takeoff
    def takeoff(self):
        self.send('takeoff')
        self.wait(10)

    # Auto landing
    def land(self):
        self.send('land')
        self.wait(10)

    # Enable video stream
    def streamon(self):
        self.send('streamon')
        self.wait(1)
    
    # Disable video stream
    def streamoff(self):
        self.send('streamoff')
        self.wait(1)

    # Ascend to x[cm] (20≤x≤100)
    def up(self, x=50):
        self.dist = max(20, min(x, 100))
        self.send('up ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)

    # Descend to x[cm] (20≤x≤100)
    def down(self, x=50):
        self.dist = max(20, min(x, 100))
        self.send('down ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)

    # Fly left for x[cm] (20≤x≤500)
    def left(self, x=100):
        self.dist = max(20, min(x, 500))
        self.send('left ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)

    # Fly right for x[cm] (20≤x≤500)
    def right(self, x=100):
        self.dist = max(20, min(x, 500))
        self.send('right ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)

    # Fly forward for x[cm] (20≤x≤500)
    def forward(self, x=100):
        self.dist = max(20, min(x, 500))
        self.send('forward ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)

    # Fly back for x[cm] (20≤x≤500)
    def back(self, x=100):
        self.dist = max(20, min(x, 500))
        self.send('back ' + str(self.dist))
        self.wait(ceil(self.dist/self.speed) + 2)
    
    # Rotate x[degrees] clockwise (1≤x≤360)
    def rotate_right(self, x=180):
        self.angle = max(1, min(x, 360))
        self.send('cw ' +  str(self.angle))
        self.wait(ceil(self.angle/50) + 2)
    
    # Rotate x[degrees] counter-clockwise (1≤x≤360)
    def rotate_left(self, x=180):
        self.angle = max(1, min(x, 360))
        self.send('ccw ' + str(self.angle))
        self.wait(ceil(self.angle/50) + 2)

    # Roll in the left direction
    def flip_left(self):
        self.send('flip l')
        self.wait(4)

    # Roll in the right direction
    def flip_right(self):
        self.send('flip r')
        self.wait(4)

    # Roll in the forward direction
    def flip_forward(self):
        self.send('flip f')
        self.wait(4)

    # Roll in the back direction
    def flip_back(self):
        self.send('flip b')
        self.wait(4)
    
    # 
    # SETTING COMMANDS
    # 

    # Set the current speed to x[cm/s] (50≤x≤100)
    def set_speed(self, x=100):
        self.speed = max(50, min(x, 100))
        self.send('speed ' + str(self.speed))
        self.wait(1)

    # 
    # OPTIONAL COMMAND
    # 

    # Take a picture
    def picture(self):
        try:
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
        except Exception as error:
            print(error)
