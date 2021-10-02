__all__ = [
    'get_img_url',
    'get_dimensions',
    'set_img_url'
]

import os
import cv2

_URL = None

# set the url
def set_img_url():
    global _URL
    _URL = input('Enter URL: ')
    _URL = os.path.abspath(_URL)

# return the url
def get_img_url():
    return _URL

# return the image dimensions
def get_dimensions(img_path):
    img = cv2.imread(img_path)
    dimensions = img.shape
    return dimensions