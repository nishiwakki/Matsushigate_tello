# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.set_speed(50)
    d.takeoff()
    d.forward(200)
    d.land()

if __name__ == "__main__":
    action()