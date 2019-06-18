import numpy as np


class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.px = x
        self.x = x
        self.y = y
        self.z = z

    def normalize(self, axis=-1, order=2):
        ### https://deepage.net/features/numpy-normalize.html
        v = np.array([self.x, self.y, self.z])
        l2 = np.linalg.norm(v, ord = order, axis=axis, keepdims=True)
        l2[l2==0] = 1
        return v/l2

    def distance(self):
        v = np.array([self.x, self.y, self.z])
        return np.linalg.norm(v)
