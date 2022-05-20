# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    d = Drone()
    d.takeoff()
    d.up()
    d.down()
    d.land()

if __name__ == "__main__":
    action()