# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.flip_forward()
    d.flip_back()
    d.flip_left()
    d.flip_right()
    d.land()

if __name__ == "__main__":
    action()