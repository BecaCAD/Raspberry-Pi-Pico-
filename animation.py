from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

WIDTH = 128
HEIGHT = 64

images = []

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

# display.invert(1)
#display.contrast(100)


images = []
for n in range(1,28):
    with open('/youtube/image%s.pbm' % n, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 64, 64, framebuf.MONO_HLSB)
    images.append(fbuf)
    


while True:
    for i in images:
        display.blit(i, 32, 0)
        display.show()
        time.sleep(0.01)

