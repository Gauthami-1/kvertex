import cv2 as cv
import numpy as np
from time import time
from mss import mss

#stores current time to calculate FPS in loop
loop_time = time()

with mss() as sct:
    monitor = {"top": (3024//2)-50, "left": (1964//2)-50, "width": 100, "height": 100}   # middle 100 pixels

    while(True):

        screenshot = np.array(sct.grab(monitor))  #captures screenshot
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)  #convertes image from RGB to BGR (needed for OpenC

        #new window shows live feed
        cv.imshow('Computer Vision', screenshot)

        #infinite loop
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        #stop when q is pressed 
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


print('Done.')
