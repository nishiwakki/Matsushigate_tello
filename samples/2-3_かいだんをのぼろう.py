# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.forward(50)
    for i in range(3):
        d.up(25)
        d.forward(50)
    d.land()

if __name__ == "__main__":
    action()