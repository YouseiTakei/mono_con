### import processing.serial.*
### import cc.arduino.*



### python
None
### my created
from graph   import Graph
from vector  import Vector




def setup():
    global graph_x, graph_y, graph_z
    graph_x = Graph()
    graph_y = Graph()
    graph_z = Graph()
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
    if frame >1000: frame = 0
    v = Vector( sin(frame), sin(frame-10), sin(frame+ 10))
    ### render graph -------------------------------------
    graph_x.update( frame, v.x )
    graph_y.update( frame, v.y )
    graph_z.update( frame, v.z )

    graph_x.render()
    graph_y.render()
    graph_z.render()

if __name__ == '__main__':
    setup()
    while True:
        try:
            draw()
        except KeyboardInterrupt:
            break
    plt.close() # 画面を閉じる
