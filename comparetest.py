# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import math
import time
from PIL import Image


cap = cv2.VideoCapture(0)
t_end = time.time() + 5
while time.time() < t_end:
    ret, img = cap.read()
    cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
    crop_img = img[100:300, 100:300]
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Thresholded', thresh1)

    #cv2.imshow('drawing', drawing)
    #cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
ret, img = cap.read()
cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
crop_img = img[100:300, 100:300]
grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
value = (35, 35)
blurred = cv2.GaussianBlur(grey, value, 0)
_, thresh1 = cv2.threshold(blurred, 127, 255,
                       cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Thresholded', thresh1)
cv2.imshow('Gesture', img)

im = Image.fromarray(thresh1)
im.save("user.jpeg")

  
    
    
def mse(imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        
        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err
        
user = cv2.imread("user.jpeg")
user = cv2.cvtColor(user, cv2.COLOR_BGR2GRAY)
rootdir = 'test'


        
def compare_images(imageA, imageB, title):
        # compute the mean squared error and structural similarity
        # index for the images
        m = mse(imageA, imageB)
        s = ssim(imageA, imageB)

        
        # setup the figure
        fig = plt.figure()
        plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    
           # show first image
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(imageA, cmap = plt.cm.gray)
        plt.axis("off")
    
           # show the second image
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(imageB, cmap = plt.cm.gray)
        plt.axis("off")
    
           # show the images
        plt.show()
        
least_MSE=20000000
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_name = os.path.join(subdir, file)
        imageB = cv2.imread(file_name)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        if mse(user, imageB)<least_MSE:
            least_MSE=mse(user, imageB)
            similar_file_name=file_name
            
print similar_file_name[5]
imageB = cv2.imread(similar_file_name)
imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
compare_images(user,imageB , similar_file_name)
# load the images -- the original, the original + contrast,
# and the original + photoshop

#contrast = cv2.imread("images/realdueces.png")
#shopped = cv2.imread("images/what.png")

# convert the images to grayscale
#original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
#shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
#fig = plt.figure("Images")
#images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)

## loop over the images
#for (i, (name, image)) in enumerate(images):
#	# show the image
#	ax = fig.add_subplot(1, 3, i + 1)
#	ax.set_title(name)
#	plt.imshow(image, cmap = plt.cm.gray)
#	plt.axis("off")

## show the figure
#plt.show()

# compare the images
#compare_images(original, original, "Original vs. Original")
#compare_images(original, contrast, "Original vs. Contrast")
#compare_images(original, shopped, "Original vs. Photoshopped")
