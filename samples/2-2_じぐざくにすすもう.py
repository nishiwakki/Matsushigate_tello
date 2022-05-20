# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.rotate_right(45)
    d.forward(50)
    d.rotate_left(90)
    d.forward(50)
    d.rotate_right(90)
    d.forward(50)
    d.rotate_left(90)
    d.forward(50)
    d.land()

if __name__ == "__main__":
    action()