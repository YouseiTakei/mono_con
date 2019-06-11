### import processing.serial.*
### import cc.arduino.*



### python
None
### my created
import math
import pyfirmata

from graph   import Graph
from vector  import Vector
from matplotlib import pyplot as plt



def setup():

    plt.ion()           # 対話モードオン
    ###  ------------------------------------------------
    global graph_x, graph_y, graph_z
    graph_x = Graph()
    graph_y = Graph()
    ### graph_z = Graph()
    ###  ------------------------------------------------
    global arduino
    arduino = pyfirmata.Arduino('COM3')

    global frame
    frame = 0

def draw():
    ### draw init ----------------------------------------
    '''
    v = PVector(0, 0, 0)
    v.x = arduino.analogRead( 0 )
    v.y = arduino.analogRead( 1 )
    v.z = arduino.analogRead( 2 )
    v.normalize()
    '''
    global frame
    frame = frame + 1
    v = Vector( math.sin(frame), math.sin(frame-10), math.sin(frame+ 10))

    ### render graph -------------------------------------
    graph_x.update( frame, v.x )
    graph_y.update( frame, v.y )
    ### graph_z.update( frame, v.z )

    graph_x.render(1)
    graph_y.render(2)
    ### graph_z.render(3)
    plt.draw()

    plt.pause(0.01)
    plt.clf()

if __name__ == '__main__':
    setup()
    while True:
        try:
            draw()
        except KeyboardInterrupt:
            break
    plt.close() # 画面を閉じる
