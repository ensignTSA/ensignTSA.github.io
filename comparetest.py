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
import random

def Aneesh():
    cap = cv2.VideoCapture(0)
    t_end = time.time() + 3
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
    
    
        
def compare(input_letter):
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

            

    MSE={}
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_name = os.path.join(subdir, file)
            imageB = cv2.imread(file_name)
            imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            MSE[file_name]=(mse(user, imageB))

    MSE_range = max(MSE.values()) - min(MSE.values())
    ten_percent = MSE_range/5
    ten_percent_limit = min(MSE.values()) + (MSE_range/10)
    
    match=False
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_name = os.path.join(subdir, file)
            imageB = cv2.imread(file_name)
            imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            if min(MSE.values()) <= mse(user, imageB) <= ten_percent_limit:
                if file_name[5]==input_letter:
                    match=True
    
    if match==True:
        cap = cv2.VideoCapture(0)
        t_end = time.time() + 2
        while time.time() < t_end:
            ret, img = cap.read()
            cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
            cv2.putText(img,"Correct!!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            cv2.imshow('Gesture', img)
            k = cv2.waitKey(10)
            if k == 27:
                break
    else:
        cap = cv2.VideoCapture(0)
        t_end = time.time() + 2
        while time.time() < t_end:
            ret, img = cap.read()
            cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
            cv2.putText(img,"Wrong!!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            cv2.imshow('Gesture', img)
            k = cv2.waitKey(10)
            if k == 27:
                break
                
def give_letter(input_letter):
    cap = cv2.VideoCapture(0)
    t_end = time.time() + 1
    while time.time() < t_end:
        ret, img = cap.read()
        cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
        out_statement = str("Please make "+input_letter)
        cv2.putText(img,out_statement, (100,75), cv2.FONT_HERSHEY_SIMPLEX, 2, 6,2)
        cv2.imshow('Gesture', img)
        k = cv2.waitKey(10)
        if k == 27:
            break

letters=[]
rootdir = 'test'
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_name = os.path.join(subdir, file)
            letters.append(file_name)


for i in range(5):
    input_letter = random.choice(letters)
    input_letter = str(input_letter[5])
    give_letter(input_letter)
    Aneesh()
    compare(input_letter.upper())
