import numpy as np


class Vector():
    def __init__(self, vx=0, vy=0, vz=0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def normalize(self, axis=-1, order=2):
        ### https://deepage.net/features/numpy-normalize.html
        v = np.array([self.vx, self.vy, self.vz])
        l2 = np.linalg.norm(v, ord = order, axis=axis, keepdims=True)
        l2[l2==0] = 1
        return v/l2
