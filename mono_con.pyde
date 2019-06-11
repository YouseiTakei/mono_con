### import processing.serial.* 
### import cc.arduino.* 



### python
import sys
### arduino
'''
add_library('serial')
add_library('arduino')
'''
### my created
from scatter import Scatter

global time
time = 0

def setup(): 
    size( 800, 300 ) 
    ### arduino  -----------------------------------------
    ### arduino = Arduino(this, 'COM1', 57600)
    ### arduino = Arduino( this, Arduino.list()[ 4 ], 57600 ) 

    global scatter_x, scatter_y, scatter_z
    scatter_x = Scatter(0,          0, width, height/3)
    scatter_y = Scatter(0, height  /3, width, height/3)
    scatter_z = Scatter(0, height*2/3, width, height/3)
    
    ### option
    scatter_x.size(width, height)
    scatter_y.size(width, height)
    scatter_z.size(width, height)
    scatter_x.color(200,   0,   0)
    scatter_y.color(  0, 150,   0)
    scatter_z.color(  0,   0, 200)
    
def draw(): 
    ### draw init ----------------------------------------
    background( color(255, 255, 255) ) 
    v = PVector(0, 0, 0)
    '''
    v.x = arduino.analogRead( 0 )
    v.y = arduino.analogRead( 1 ) 
    v.z = arduino.analogRead( 2 )
    v.normalize()
    '''
    global time
    time = time + 1 
    if time >1000: time = 0
    v = PVector( sin(time), sin(time-10), sin(time+ 10))
    ### render graph -------------------------------------
    scatter_x.update( v.x )
    scatter_y.update( v.y )
    scatter_z.update( v.z )
    
    scatter_x.render()
    scatter_y.render()
    scatter_z.render()
