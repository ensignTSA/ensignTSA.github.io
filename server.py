from bottle import static_file,route,run,request
import json
import os
@route('/')
def loadIndex():
    return static_file('index.html', root='./') #sets up web page
@route('/<filename:re:.*\..*>')#matches files
def sendWebFile(filename):
    return static_file(filename, root='./')
@route('/postBooks',method='POST') #gets input from fancyform, sends book data to JSON
def postBooks():
    
    bookName=request.forms.get('bookName') #get book name from form
    author=request.forms.get('author') #get author from form
    subject=request.forms.get('subject') #get subject from form
    condition=request.forms.get('condition') #get condition from form
    name=request.forms.get('name') #get name from form
    phoneNumber=request.forms.get('phoneNumber') #get phone number from form
    email=request.forms.get('email') #get email from form
    if(bookName!="" and name!=""):
        f=open('tradedata.json','r+') #opens the json
        data = f.read();
        data = data.replace("]}",",") #formats the json
        f.truncate(0)
        g=open('tradedata.json','a')
        g.write(data)
        #prints data into json
        g.write('{"bookName":"'+bookName+'","author":"'+author+'","subject":"'+subject+'","condition":"'+condition+'","name":"'+name+'","phoneNumber":"'+phoneNumber+'","email":"'+email+'"}]}')
        return "Thank you very much!" #server interaction is complete
run(host='localhost',port=8080,debug=True)
