# Detailed explanation at http://hitesh.in/2011/running-a-bottle-py-app-on-dreamhost/

#1. Add current directory to path, if isn't already 
from urllib2 import HTTPError
import os, sys
import bottle
import comparetest

from PIL import Image
cmd_folder = os.path.dirname(os.path.abspath(__file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from bottle import static_file,route,run,request,redirect

#2. Define needed routes here	
@route('/')
def loadIndex():
    return static_file('index.html', root='./') #sets up web page
    
def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)

#4. Main method for local developement	
if __name__ == "__main__":
