from inputHelper import *

def main():
    set_img_url()
    url = get_img_url()
    dims = get_dimensions(url)
    print("Input Dimensions are",dims)

main()