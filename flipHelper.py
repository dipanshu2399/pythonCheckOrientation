__all__ = [
    'flip_img'
]

import numpy as np
import cv2

_cnt = None

def flip_img(img):
    img = cv2.transpose(img)
    img_counter = get_cnt()
    cv2.imwrite("./flipped-images/image_"+str(img_counter+1)+".png",img)
    inc_cnt()

def get_cnt():
    global _cnt
    fp = open('./flipped-images/cnt.txt','r')
    _cnt = int(fp.readlines()[0])
    return _cnt

def inc_cnt():
    global _cnt
    fp = open('./flipped-images/cnt.txt','w')
    fp.write(str(_cnt+1))
    return