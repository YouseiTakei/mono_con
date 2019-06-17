from pyfirmata2 import Arduino
import time

# self.port = Arduino.AUTODETECT
# self.port = '/dev/ttyACM0'

# prints data on the screen at the sampling rate of 50Hz
# can easily be changed to saving data to a file

class Reader:
    class Analog:
        def __init__(self, pin, _board):
            ### base ----------------
            self._board    = _board
            self.timestamp = 0
            ### data-----------------
            self.pin       = pin
            self.value     = 0
            self.callback  = None
            ### ---------------------
        def print_value(self, data):
            print("%f,%f" % (self.timestamp, data))
            self.timestamp += (1 / self.samplingRate)
            self.set_value(data)
        def set_value(self, data):
            self.value = data

    def __init__(self, port='/dev/ttyUSB0'):
        ### base ----------------------
        self.port  = port
        self.board = Arduino(self.port)
        ### data ---------------------
        self.analog       = {}
        self.samplingRate = 10
        ### setup --------------------
        self.board.samplingOn(100/self.samplingRate)

    ### void setup -------------------------------------------------------------
    def start(self, pin=0, callback=None):
        self.analog[pin] = self.Analog(pin, self.board)
        if callback: self.analog[pin].callback= callback
        else       : self.analog[pin].callback= self.analog[pin].set_value
        self.board.analog[pin].register_callback(self.analog[pin].callback)
        self.board.analog[pin].enable_reporting()

    ### void draw --------------------------------------------------------------
    def stop(self):
        self.board.samplingOff()
        self.board.exit()

if __name__ == '__main__':
    reader = Reader('COM3')

    reader.start(0)
    reader.start(1)

    epoch = 0
    while True:
        epoch += 1
        time.sleep(0.01)
        print(epoch)
        print('0', reader.analog[0].value)
        print('1', reader.analog[0].value)
        if epoch >1000: break;


    # let's stop it
    reader.stop()

    print("finished")
