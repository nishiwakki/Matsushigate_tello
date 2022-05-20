# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.rotate_left(45)
    for i in range(3):
        d.flip_forward()
    for i in range(3):
        d.flip_right()
    for i in range(3):
        d.flip_back()
    for i in range(3):
        d.flip_left()
    d.land()

if __name__ == "__main__":
    action()