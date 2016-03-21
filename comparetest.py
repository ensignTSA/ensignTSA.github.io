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
import win32api


#open camera window and detect sign made
def read_letter(input_letter):
   cap = cv2.VideoCapture(0)
   t_end = time.time() + 4
   #display camera window for 4 seconds for user to make sign
   while time.time() < t_end:
       ret, img = cap.read()
       #Display area for user to make sign
       cv2.rectangle(img,(300,300),(100,100),(255,255,255),0)
       #Add prompt statement with corresponding sign
       out_statement = str("Please make the sign "+input_letter+".")
       cv2.putText(img,out_statement, (25,75), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255),2)
       #Display camera window
       try:
           cv2.imshow('Sign', img)
       except:
           win32api.MessageBox(0,"","You don't appear to have a webcamera.")
           sys.exit()
        #Necessary wait key for image to appear
       k = cv2.waitKey(10)
       if k == 27:
           cv2.destroyAllWindows()
           sys.exit()
           break
   #After user has had time to make sign, read final camera image
   ret, img = cap.read()
   cv2.rectangle(img,(300,300),(100,100),(255,255,255),0)
   #crop the area the user made the sign in 
   crop_img = img[100:300, 100:300]
   #convert to greyscale to remove effect of uneven coloring and lighting
   grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
   value = (35, 35)
   #blur the image to smooth image and reduce background noise and details
   blurred = cv2.GaussianBlur(grey, value, 0)
   #Use OpenCV's Otsu's Binarization thresholding method
   #to detect important structures and disregard background
   _, thresh1 = cv2.threshold(blurred, 127, 255,
                       cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
   try:
       cv2.imshow('Sign', img)
   except:
       win32api.MessageBox(0,"","You don't appear to have a webcamera.")
       sys.exit()
   #save cropped image in root folder
   im = Image.fromarray(thresh1)
   im.save("user.jpeg")
   

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
   user = cv2.imread("user.jpeg")
   user = cv2.cvtColor(user, cv2.COLOR_BGR2GRAY)
   rootdir = 'test'
            
   MSE={}
   #For each test file, add to the MSE dictionary
   #Key: file name
   #Value:MSE between test image and user image
   for subdir, dirs, files in os.walk(rootdir):
       for file in files:
           file_name = os.path.join(subdir, file)
           imageB = cv2.imread(file_name)
           imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
           MSE[file_name]=(mse(user, imageB))
    
   #Find range of MSE values and lowest 20% of MSE values
   MSE_range = max(MSE.values()) - min(MSE.values())
   lowest_percent = MSE_range/4
   #MSE value at 20th percentile
   lowest_percent_limit = min(MSE.values()) + (lowest_percent)
   
   match=False
   for file_name in MSE.keys():
        imageB = cv2.imread(file_name)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        #if MSE value between test image and user image 
        #falls between lowest 20%
        if min(MSE.values()) <= mse(user, imageB) <= lowest_percent_limit:
           #if that test image corresponds with desired letter
           if file_name[5]==input_letter:
               match=True
   
   if match==True:
       cap = cv2.VideoCapture(0)
       t_end = time.time() + 1
       #for one second, display camera window 
       while time.time() < t_end:
           ret, img = cap.read()
           cv2.rectangle(img,(300,300),(100,100),(255,255,255),0)
           #Add "Correct" in green text
           cv2.putText(img,"Correct.", (100,75), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0),2)
           try:
              cv2.imshow('Sign', img)
           except:
              win32api.MessageBox(0,"","You don't appear to have a webcamera.")
              sys.exit()
           #Add necessary wait key for image to appear
           k = cv2.waitKey(10)
           if k == 27:
               cv2.destroyAllWindows()
               sys.exit()
               break
   else:
       cap = cv2.VideoCapture(0)
       t_end = time.time() + 1
       #for one second, display camera window 
       while time.time() < t_end:
           ret, img = cap.read()
           cv2.rectangle(img,(300,300),(100,100),(255,255,255),0)
           #Display incorrect text in red letters
           cv2.putText(img,"Wrong; Try Again.", (100,75), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255),2)
           try:
               cv2.imshow('Sign', img)
           except:
               win32api.MessageBox(0,"","You don't appear to have a webcamera.")
               sys.exit()
           #Add necessary wait key
           k = cv2.waitKey(10)
           if k == 27:
               cv2.destroyAllWindows()
               sys.exit()
               break
       #Rerun read and compare functions on same input letter
       #until the user gets sign correct
       read_letter(input_letter)
       compare(input_letter.upper())


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
