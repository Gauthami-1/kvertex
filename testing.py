# install this for rasberry pi
# pip install rpi-ws281x

import time
import numpy as np
import config
from rpi_ws281x import Adafruit_NeoPixel

# Initialize the LED strip
strip = Adafruit_NeoPixel(config.N_PIXELS, config.LED_PIN,
                          config.LED_FREQ_HZ, config.LED_DMA,
                          config.LED_INVERT, config.BRIGHTNESS)
strip.begin()

def set_color(color):
    """Set all LEDs to the same color (RGB format)"""
    for i in range(config.N_PIXELS):
        strip.setPixelColor(i, (color[0] << 16) | (color[1] << 8) | color[2])
    strip.show()

print("Starting LED test...")

# **Color Test Sequence**
test_colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 255),  # White
    (0, 0, 0)  # Off
]

for color in test_colors:
    print(f"Setting LEDs to {color}")
    set_color(color)
    time.sleep(1)  # Hold each color for 1 second

print("LED test complete!")
