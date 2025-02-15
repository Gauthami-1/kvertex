import cv2 as cv
import numpy as np
from time import time
from mss import mss

loop_time = time()

with mss() as sct:
    screen_width = sct.monitors[1]["width"]
    screen_height = sct.monitors[1]["height"]

    monitor = {
        "top": screen_height // 2 - 50,
        "left": screen_width // 2 - 50,
        "width": 100,
        "height": 100
    }

    while True:
        screenshot = np.array(sct.grab(monitor))
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        cv.imshow('Computer Vision', screenshot)

        print('FPS {:.2f}'.format(1 / (time() - loop_time)))
        loop_time = time()

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

print('Done.')
