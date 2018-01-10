import cv2
import numpy as np
import sys

img = Image.open(sys.argv[1])

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)