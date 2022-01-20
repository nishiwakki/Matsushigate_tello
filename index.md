### ドローンPythonプログラミング
## 松茂から徳島を救え! ドローンの動きをプログラミングしよう!

***

- ドローンを動かすためには，**startpy** の **action関数** の中身をプログラミングする必要があります。

```python
# -*- coding: utf-8 -*-

from Tello_api import Drone

def action():
    drone = Drone()
    # この部分をプログラミングします

if __name__ == "__main__":
    action()
```

***

- 以下のメソッドを使ってドローンを動かすことができます。

| メソッド名 | 引数 | 説明 |
| :---: | :--- | :--- |
| **`takeoff()`** | - | Auto takeoff |
| **`land()`** | - | Auto landing |
| **`up(x)`** | 20≤x≤500 | Ascend to x[cm] |
| **`down(x)`** | 20≤x≤500 | Descend to x[cm] |
| **`left(x)`** | 20≤x≤500 | Fly left for x[cm] |
| **`right(x)`** | 20≤x≤500 | Fly right for x[cm] |
| **`forward(x)`** | 20≤x≤500 | Fly forward for x[cm] |
| **`back(x)`** | 20≤x≤500 | Fly back for x[cm] |
| **`rotate(x)`** | 1≤x≤360 | Rotate x[degrees] |
| **`picture()`** | - | Take a picture |

***
