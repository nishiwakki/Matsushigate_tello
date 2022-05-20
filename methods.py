# -*- coding: utf-8 -*-

from samples.Tello_api import Drone

# ドローンをうごかすためにひつようです
d = Drone()

# ドローンを「りりく」させます
d.takeoff()

# ドローンを「ちゃくりく」させます
d.land()

# ドローンを「うえ」にうごかします
d.up()

# ドローンを「した」にうごかします
d.down()

# ドローンを「ひだり」にうごかします
d.left()

# ドローンを「みぎ」にうごかします
d.right()

# ドローンを「まえ」にうごかします
d.forward()

# ドローンを「うしろ」にうごかします
d.back()

# ドローンを「ひだり」かいてんさせます
d.rotate_left()

# ドローンを「みぎ」かいてんさせます
d.rotate_right()

# ドローンを「ひだり」にフリップさせます
d.flip_left()

# ドローンを「みぎ」にフリップさせます
d.flip_right()

# ドローンを「まえ」にフリップさせます
d.flip_forward()

# ドローンを「うしろ」にフリップさせます
d.flip_back()

# ドローンの「うごくスピード」をかえます
d.set_speed()

# ドローンのカメラで「しゃしん」をとります
d.picture()
