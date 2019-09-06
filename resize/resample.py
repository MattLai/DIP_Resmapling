import numpy as np
import math

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # get original image height and width
        height, width = image.shape[0], image.shape[1]
        # new height and new width
        newHeight = int(height*fy)
        newWidth = int(width*fx)

        new_image = np.zeros((newHeight, newWidth, 3), np.uint8)
        for i in range(newHeight):
            for j in range(newWidth):
                x = int(j / fx)
                y = int(i / fy)
                new_image[i, j] = image[y, x]

        return new_image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        height, width = image.shape[:2]


        newWidth = int(width * fx)
        newHeight = int(height * fy)

        new_image = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
        # insert pixel to new image.
        for i in range(newHeight):
            for j in range(newWidth):

                x = (j + 0.5) / fx - 0.5
                y = (i + 0.5) / fy - 0.5

                x1 = int(np.floor(x))
                y1 = int(np.floor(y))
                x2 = min(x1 + 1, width - 1)
                y2 = min(y1 + 1, height - 1)

                # bi-linear
                new_image[i, j] = int(((y2 - y)/(y2 - y1) * ((x2 - x)/(x2-x1) * image[y1, x1] + (x - x1)/(x2-x1) * image[y1, x2]))
                                      + (y - y1)/(y2-y1) * ((x2 - x)/(x2-x1) * image[y2, x1] + (x - x1)/(x2-x1) * image[y2, x2]))

        return new_image
