### import processing.serial.*
### import cc.arduino.*



### python
None
### my created
import math
import numpy as np
from graph   import Graph
from vector  import Vector
from reader  import Reader
from matplotlib import pyplot as plt

from pyfirmata2 import Arduino, util
from psonic import *

def setup():
    plt.ion()           # 対話モードオン
    global frame
    frame = 0
    ###  ------------------------------------------------
    global v
    v = Vector(0, 0, 0)
    ### --------------------------------------------------
    global reader
    reader = Reader('/dev/ttyUSB0')
    ### reader = Reader('/dev/COM3')
    reader.start(0)
    reader.start(1)
    reader.start(2)
    reader.start(3)
    reader.start(4)
    ###  ------------------------------------------------
    global graph_a, graph_l, graph_r
    graph_a = Graph()
    graph_l = Graph()
    graph_r = Graph()
    graph_a.bias = 0.5
    graph_l.bias = 0.5
    graph_r.bias = 0.5
    ### --------------------------------------------------

def draw():
    global frame
    frame += 1
    ### draw init ----------------------------------------
    v.z = reader.analog[2].value
    v.y = reader.analog[3].value
    v.x = reader.analog[4].value
    ### v.normalize()
    ### render graph -------------------------------------
    graph_a.update( frame, v.distance() )
    graph_l.update( frame, reader.analog[0].value )
    graph_r.update( frame, reader.analog[1].value )

    graph_a.render(1, "dis")
    graph_l.render(3, "l")
    graph_r.render(5, "r")

    plt.draw()
    plt.pause(0.01) ### 05)
    plt.clf()

    ### if graph_x.val_y[-1] > np.std(graph_x.val_y)*3:
        ### play (60, attack=0.5, decay=1, sustain_level=0.4, sustain=0.1, release=0.1)


if __name__ == '__main__':
    setup()
    while True:
        try:
            draw()
        except KeyboardInterrupt:
            break
    plt.close() # 画面を閉じる
    reader.stop()
