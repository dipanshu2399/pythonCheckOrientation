__all__ = [
    'get_pillow_img',
    'show_pillow_img',
    'getBasicDetails'
]
_PILLOW_IMG = None
from PIL import Image


def get_pillow_img(img_url):
    global _PILLOW_IMG
    img = Image.open(img_url)
    _PILLOW_IMG = img
    return img

#show the image
def show_pillow_img():
    _PILLOW_IMG.show()

#getBasic details of image
def getBasicDetails():
    print(_PILLOW_IMG.format)
    print(_PILLOW_IMG.mode)
    

