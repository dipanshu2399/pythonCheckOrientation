from inputHelper import *

# main method
def main():
    set_img_url()
    url = get_img_url()
    dims = get_dimensions(url)
    print("Input Picture Dimensions are",dims)

main()