'''
def color(r, g, b):
    return [r, g, b]
def fill( color ):
    pass
def background(color):
    pass
def stroke(color):
    pass
def line():
    pass
def text(txt, x, y, w, h):
    pass
def point(x, y, w, h):
    pass
'''

class Scatter:
    def __init__(self,x_val,y_val,w_val=100,h_val=600):
        ### value of window--------------------------------
        self.width = 800
        self.height= 600
        ### value of scatter ------------------------------
        self.x_val = x_val
        self.y_val = y_val
        self.w_val = w_val
        self.h_val = h_val
        self.c_val = color(0, 0, 0) ### color of graph
        ### input data ------------------------------------
        self.label = ''
        self.val   = 0
        self.vals  = [0] * self.width
        self.bias  = 0
        self.arrX  = [] ### ? ?

        self.valrr_len= 100### number of graph potints
        self.firstContact = False

    ### void setup ----------------------------------------
    def size(self, width, height):
        self.width = width
        self.height= height
        self.vals  = [0]*self.width

    def color(self, r_val, g_val, b_val):
        self.c_val = color(r_val, g_val, b_val)

    ### void draw -----------------------------------------
    def update(self, new_val=0):
        self.val = new_val - self.bias
        for i in range(1, self.width):
            self.vals[i-1] = self.vals[i]
        self.vals[self.width-1] = new_val

    def render(self):
        ### init setting of render ------------------------
        fill( self.c_val)
        stroke( self.c_val )


        ### init render graph -----------------------------
        text("val: {}".format(self.val), 10, 15 + self.y_val)
        line(self.x_val,
             self.y_val+ self.h_val/2,
             self.x_val+ self.w_val,
             self.y_val+ self.h_val/2)


        ### plot the point of scatter ---------------------
        for i in range(self.width):
            stroke(self.c_val)
            point(i, -self.vals[i]* self.h_val/2 + self.y_val + self.h_val/2)


        ### write the number of range ---------------------
        fill(0)
        stroke(color(0, 0, 0))
        text(" 1", 10, self.y_val + self.h_val/2 + 5 - 30)
        text("-1", 10, self.y_val + self.h_val/2 + 5 + 30)
        text(" 0", 10, self.y_val + self.h_val/2 + 5)
        line(self.x_val,
             self.y_val+ self.h_val/2,
             self.x_val+ self.w_val,
             self.y_val+ self.h_val/2)
if __name__ == '__main__':
    scatter =
