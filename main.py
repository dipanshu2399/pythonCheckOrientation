#!python
from flipHelper import *
from inputHelper import *
from imageHelper import *

# main method
def main():
    set_img_url()
    url = get_img_url()
    set_img(url)
    img = get_img()
    dims = get_dimensions(img)
    set_dims(dims)
    img_type = get_type()
    print("Type of image",img_type)
    flipd_dec = input("do you wish to toggle img type? (yes/no) ")
    if(flipd_dec == "yes"):
        print("Flipping Image...")
        flip_img(img)
main()