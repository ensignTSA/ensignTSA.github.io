# Detailed explanation at http://hitesh.in/2011/running-a-bottle-py-app-on-dreamhost/

#1. Add current directory to path, if isn't already 
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import math
import time
import random
import os, sys
import bottle
from PIL import Image
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from bottle import static_file,route,run,request

#2. Define needed routes here	
@route('/')
def loadIndex():
    return static_file('index.html', root='./') #sets up web page
    
@route('/<filename:re:.*\..*>')#matches files
def sendWebFile(filename):
    return static_file(filename, root='./')
    
@route('/runScript',method = "POST")
def script():
    execfile('comparetest.py')

@route('/<fn:path>')
def index(fn='index.html'):
    return bottle.static_file(fn, root='./static')


def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)

#4. Main method for local developement	
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)