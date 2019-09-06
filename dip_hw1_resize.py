"""dip_hw1.py: Starter file to run howework 1"""

#Example Usage: ./dip_hw1_resize.py -i imagename.jpg -fx 1.5 -fy = 1.5 -m nearest_neighbor
#Example Usage: ./dip_hw1_resize.py -i imagename.jpg -fx 1.5 -fy = 1.5 -m bilinear
# Or:
#Example Usage: python dip_hw1_resize.py -i imagename.jpg -fx 1.5 -fy = 1.5 -m nearest_neighbor
#Example Usage: python dip_hw1_resize.py -i imagename.jpg -fx 1.5 -fy = 1.5 -m bilinear

__author__      = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
# from resize import resample
from datetime import datetime
from resize import resample


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     interpolation method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-fx", "--resize_x", dest="resize_x",
                        help="specify scale size (fx)", metavar="RESAMPLE SIZE")
    parser.add_argument("-fy", "--resize_y", dest="resize_y",
                        help="specify scale size (fy)", metavar="RESAMPLE SIZE")
    parser.add_argument("-m", "--interpolation", dest="interpolate",
                        help="specify the interpolation method (nearest_neighbor or bilinear)", metavar="INTERPOLATION METHOD")

    args = parser.parse_args()
	
    #Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    #Check resize scale parametes
    if args.resize_x is None:
        print("Resize scale fx not specified using default (1.5)")
        print("use the -h option to see usage information")
        fx = 1.5
    else:
        fx = args.resize_x

    if args.resize_y is None:
        print("Resize scale fy not specified using default (1.5)")
        print("use the -h option to see usage information")
        fy = 1.5
    else:
        fy = args.resize_y
	

    #Check interpolate method argument
    
    if args.interpolate is None:
        print("Interpolation method not specified, using default=nearest_neighbor")
        print("use the -h option to see usage information")
        interpolation = "nearest_neighbor"

    else:
        if args.interpolate not in ["nearest_neighbor", "bilinear"]:
            print("Invalid nterpolation method, using default=nearest_neighbor")
            print("use the -h option to see usage information")
            interpolation = "nearest_neighbor"
        else:
            interpolation = args.interpolate


    resample_obj = resample.resample()
    resampled_image = resample_obj.resize(input_image, fx=fx, fy=fy, interpolation=interpolation)

    #Write output file
    outputDir = 'output/resize/'

    output_image_name = outputDir+image_name+interpolation+datetime.now().strftime("%m%d-%H%M%S")+".jpg"    
    cv2.imwrite(output_image_name, resampled_image)


if __name__ == "__main__":
    main()







