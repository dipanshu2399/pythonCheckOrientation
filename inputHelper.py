__all__ = [
    'get_img_url',
    'get_dimensions',
    'set_img_url'
]

import os
import cv2

_URL = None

def set_img_url():
    _URL = input('Enter URL:')
    _URL = os.path.abspath(_URL)

def get_img_url():
    return _URL


def get_dimensions(img_path):
    img = cv2.imread(img_path)
    dimensions = img.shape
    return dimensions