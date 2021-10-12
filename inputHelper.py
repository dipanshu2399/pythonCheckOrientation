__all__ = [
    'get_img_url',
    'get_dimensions',
    'set_img_url',
    'get_img',
    'set_img'
]

import os
import cv2
import tkinter as tk
from tkinter import filedialog

_URL = None
_IMG = None

# set the url
def set_img_url():
    global _URL
    print("choose file from file explorer")
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    print(filename)
    _URL = os.path.abspath(filename)

# return the url
def get_img_url():
    global _URL
    return _URL

# set the image object
def set_img(img_url):
    global _IMG
    _IMG = cv2.imread(img_url)

# get the img obj
def get_img():
    global _URL
    return _IMG

# return the image dimensions
def get_dimensions(img):
    dimensions = img.shape
    return dimensions