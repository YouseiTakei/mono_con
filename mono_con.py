#! python3
#-*- coding: utf-8 -*-

""" ものコン用スクリプト

Usage:
    $ python3 mono_con.py --graph

"""

### import processing.serial.*
### import cc.arduino.*

import argparse
import pygame
### from pygame.locals import *
import numpy as np
from matplotlib    import pyplot as plt
### from pyfirmata2    import Arduino, util
### from psonic        import *

### my created
from graph   import Graph
from vector  import Vector
from reader  import Reader

def setup():
    global args
    args = get_args()

    plt.ion()           # 対話モードオン

    global frame ### frame number
    frame = 0
    ###  ------------------------------------------------
    global v ### , v1
    v = Vector(0, 0, 0)
    ### v1 = Vector(0, 0, 0)
    ### --------------------------------------------------
    ### initialize reader
    global reader
    reader = Reader(args.port)
    reader.start(0) ### left bending sensor
    reader.start(1) ### right bending sensor
    reader.start(2) ### Acceleration in the z-axis direction
    reader.start(3) ### Acceleration in the y-axis direction
    reader.start(4) ### Acceleration in the x-axis direction
    ###  ------------------------------------------------
    ### initialize graph
    global graph_a, graph_l, graph_r
    graph_a = Graph() ### Acceleration
    graph_l = Graph() ### left bending sensor value
    graph_r = Graph() ### right bending sensor value
    graph_a.bias = 0.5
    graph_l.bias = 0.5
    graph_r.bias = 0.5
    ### --------------------------------------------------
    ### initialize sound
    global sound
    pygame.mixer.init(frequency=22050, size=8, channels=1, buffer=1024)
    sound = pygame.mixer.Sound(args.file)

def draw():
    global frame
    frame += 1
    ### get current sensor value -------------------------
    b_l = reader.analog[0].value
    b_r = reader.analog[1].value
    v.z = reader.analog[2].value
    v.y = reader.analog[3].value
    v.x = reader.analog[4].value
    ### v.normalize()
    ### render graph -------------------------------------
    graph_a.update(frame, v.distance())
    graph_l.update(frame, b_l)
    graph_r.update(frame, b_r)

    if args.graph:
        graph_a.render(1, "dis")
        graph_l.render(3, "l")
        graph_r.render(5, "r")

        plt.draw()
        plt.pause(0.01) ### 05)
        plt.clf()

    ### Judgment of how to sweep -------------------------
    b_a = np.std(graph_a.val_y[-3:]) > 0.01
    b_l = graph_l.val_y[-2] - graph_l.val_y[-1] > 0.05
    b_r = graph_r.val_y[-2] - graph_r.val_y[-1] > 0.05
    b_result = b_a and (b_l or b_r)

    if frame < 50:
        return 0

    if args.log:
        print('a: {:5}, l: {:5}, r: {:5}, all: {:5}'.format(b_a, b_l, b_r, b_result))

    if  b_result:
        if args.log:
            print('success')
        sound.play()

def get_args():
    parser = argparse.ArgumentParser(description='This script is developed for mono con at 2019.')
    parser.add_argument('--graph',
                        action='store_true',
                        help='show graph')
    parser.add_argument('--log',
                        action='store_true',
                        help='show log')
    parser.add_argument('--port',
                        type=str, default='/dev/ttyACM0',
                        help='set connected port, default is /dev/ttyACM0')
    parser.add_argument('--file',
                        type=str,
                        default='sound/machdash1.wav',
                        help='specify sound file path, default is sound/machdash1.wav')

    return parser.parse_args()

def main():
    setup()
    while True:
        try:
            draw()
        except KeyboardInterrupt:
            break
    plt.close() # 画面を閉じる
    reader.stop()
    pygame.mixer.quit()

if __name__ == '__main__':
    main()
