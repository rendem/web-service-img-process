import numpy as np
import argparse
import cv2
from PIL import Image
from skimage import io
import scipy
from scipy import misc

# def process_image():
# FILE_PATH = '.static/images/'
ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help="path to the image")
# Image.open("data/messi.jpg")

image = cv2.imread("a.png")

boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("image", np.hstack([image, output]))
    cv2.waitKey(0)


#def get_type_convert(np_type):
    #convert_type = type(np.zeros(1, np_type).tolist()[0])
   # return np_type, convert_type


#for i in range(image.shape[0]):
    #for k in range(image.shape[1]):
        #if image[i, k, 0] == 0 and image[i, k, 1] == 0 and image[
            #i, k, 2] == 0:  # 0 is R, 1 is G, 2 is B, i and k is each rown and column of pixels.
           # print("Pixel [%d|%d] black" % (i, k))

def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)

img = Image.open('a.png')
#img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(img)
print(average_color)
#  return colors
# def process_image(image):

# result = ''
# return result
