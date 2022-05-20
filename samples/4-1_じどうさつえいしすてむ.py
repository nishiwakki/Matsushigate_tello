# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.forward(200)
    d.rotate_right()
    d.up(25)
    d.down(50)
    d.up(25)
    d.picture()
    d.forward(200)
    d.land()

if __name__ == "__main__":
    action()