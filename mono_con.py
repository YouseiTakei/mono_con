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
    reader = Reader('COM3')
    reader.start(0)
    reader.start(1)
    reader.start(2)
    ###  ------------------------------------------------
    global graph_x, graph_y, graph_z
    graph_x = Graph()
    graph_y = Graph()
    graph_z = Graph()
    graph_x.bias = 0.5
    ### --------------------------------------------------

def draw():
    global frame
    frame += 1
    ### draw init ----------------------------------------
    v.x = reader.analog[0].value
    v.y = reader.analog[1].value
    v.z = reader.analog[2].value
    v.normalize()
    ### render graph -------------------------------------
    graph_x.update( frame, v.x )
    graph_y.update( frame, v.y )
    graph_z.update( frame, v.z )

    graph_x.render(1)
    graph_y.render(2)
    graph_z.render(3)

    plt.draw()
    plt.pause(0.01)### 05)
    plt.clf()

    if graph_x.val_y[-1] > np.std(graph_x.val_y)*3:
        play (60, attack=0.5, decay=1, sustain_level=0.4, sustain=0.1, release=0.1)


if __name__ == '__main__':
    setup()
    while True:
        try:
            draw()
        except KeyboardInterrupt:
            break
    plt.close() # 画面を閉じる
    reader.stop()
