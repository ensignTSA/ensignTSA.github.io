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

@route('/process_file',method = "POST") #processes images, sending them to temp directory
def process_file():
    f = open("public/temp.png",'wb')#opens temp for editing

    body=request.body.read();
    letter = body[0]
    body = body[1:]
    body=body.replace('imgData=data:image/jpeg;base64,','');#replaces temp with the image captured by JavaScript

    body=body.decode('base64')
    f.write(body);
    f.close();#saves temp
    if(comparetest.compare(letter)):
        return "Correct!" #sets up web page
    else:
        return "Incorrect!"
    
@route('/<filename:re:.*\..*>')#matches files
def sendWebFile(filename):
    return static_file(filename, root='./')
    
@route('/runScript',method = "POST")
def script():
    try:
        import comparetest
        comparetest.practice()
    except:
        print "hi"
        redirect('http://localhost:8080/#practice')


@route('/learnScript/<letter>')
def scropt(letter):
    try:
        import comparetest
        comparetest.learn(letter)
    except:
        
        redirect('http://localhost:8080/#learn')

@route('/<fn:path>')
def index(fn='index.html'):
    return bottle.static_file(fn, root='./static')

    
def application(environ, start_response):
    return bottle.default_app().wsgi(environ,start_response)

#4. Main method for local developement	
if __name__ == "__main__":
    run(host='0.0.0.0',port=8085,debug=True)
