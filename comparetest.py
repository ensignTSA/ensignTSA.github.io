# USAGE
# python compare.py

# import the necessary packages
import numpy as np
import cv2
import os
import math
import time
from PIL import Image
import random
import sys
import string


#compare user image and saves test images
def compare(input_letter):
   def mse(imageA, imageB):
           # the 'Mean Squared Error' between the two images is the
           # sum of the squared difference between the two images;
           err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
           err /= float(imageA.shape[0] * imageA.shape[1])
           
           # return the MSE, the lower the error, the more "similar"
           # the two images are
           return err
           
   #load saved uer image
   user = cv2.imread("temp.png",1)
   user = user[200:400,200:400]
   user = cv2.cvtColor(user, cv2.COLOR_BGR2GRAY)
   
   user = cv2.GaussianBlur(user,(35,35),0)
   _, user = cv2.threshold(user,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
   #cv2.imshow('d',user)
   rootdir = 'test'
   MSE={}
   #For each test file, add to the MSE dictionary
   #Key: file name
   #Value:MSE between test image and user image
   for subdir, dirs, files in os.walk('test'):
       for file in files:
           file_name = os.path.join(subdir, file)
           imageB = cv2.imread(file_name)
           imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
           MSE[file_name]=(mse(user, imageB))
   #Find range of MSE values and lowest 20% of MSE values
   MSE_range = max(MSE.values()) - min(MSE.values())
   lowest_percent = MSE_range/5
   #MSE value at 20th percentile
   lowest_percent_limit = min(MSE.values()) + (lowest_percent)
   match=False
   for file_name in MSE.keys():
        imageB = cv2.imread(file_name)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        #if MSE value between test image and user image 
        #falls between lowest 20%
        if file_name[5]==input_letter:
        
           #if that test image corresponds with desired letter
           print min(MSE.values())
           print mse(user,imageB)
           print lowest_percent_limit
           if min(MSE.values()) <= mse(user, imageB) <= lowest_percent_limit:
               match=True
   #print MSE
   return match
       #Rerun read and compare functions on same input letter
       #until the user gets sign correct



#practice tab   
def practice():
    #All possible signs for user to make
    alphanumerical=["0","1","2","4","5","6","7","8","9",'A',
    'B','C','D','E','F','G',"H",'I',"J",'K',"L","M","N","O",'P',"Q",'R','S',
    'T','U','V','W',"X",'Y','Z']
    #call necessary functions 36 times
    for i in range(36):
       if not alphanumerical:
           break
       else:
           input_letter = random.choice(alphanumerical)
           #remove sign from choices once done
           alphanumerical.remove(input_letter)
           read_letter(input_letter)
           compare(input_letter.upper())
       
#run functions with input letter from learn tab
def learn(input_letter):
    while 1==1:
        read_letter(input_letter)
        compare(input_letter.upper())
