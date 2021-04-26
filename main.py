from ppadb.client import Client
import time
from PIL import ImageDraw, ImageTk
import PIL.Image

import numpy as np

import cv2
from viewer import AndroidViewer


def connect_device():
    adb = Client(host='127.0.0.1',port=5037)
    devices = adb.devices()
    if len(devices) == 0:
        print("No Devices Attached")
        quit()
    return devices[0]


def resizer(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    dsize = (width, height)
    imS = cv2.resize(image, dsize)
    return imS


def masking(view, ra, name):
    lower = np.array(ra[0])
    upper = np.array(ra[1])
    hsv = cv2.cvtColor(view, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    view_height, view_width, _ = view.shape

    # cv2.imshow(name, mask)

    # cv2.waitKey(1)
    return(round(cv2.countNonZero(mask)/mask.size*100,0))


android = AndroidViewer()

def video_stream():

    resize_size = 25

    frames = android.get_next_frames()

    print(android.resolution)

    if frames is None:
        pass

    else:

        for frame in frames:


            imS = resizer(frame, resize_size)
            # print(imS.shape[0], imS.shape[1])
            sc = cv2.cvtColor(imS, cv2.COLOR_BGR2RGB)
            percentages = []




            cv2.imshow('Phone Viewer', imS)
            cv2.waitKey(1)


while True:
    video_stream()
