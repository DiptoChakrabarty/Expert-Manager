#!/usr/bin/python36

import subprocess as sp
import cgi,cgitb
import os
print("content-type: text/html")

cgitb.enable()


import cv2
import numpy as np
import webbrowser

models=[]
profiles=[]

#read profiles from profiles file
f=open('profiles','r')
for line in f:
	line=line[:-1]
	profiles.append(line)
f.close()


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    
	# Convert image to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, 1.3, 5)
	if faces is ():
	    return img, []

	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
	    roi = img[y:y+h, x:x+w]
	    roi = cv2.resize(roi, (200, 200))
	return img, roi


try:
	frame = cv2.imread('image.jpg')

	image, face = face_detector(frame)


	face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

	# Pass face to prediction model
	# "results" comprises of a tuple containing the label and the confidence value

	results_models=[]
	confidence_models=[]

	for i in range(len(profiles)):		
		model=cv2.face_LBPHFaceRecognizer.create()
		model.read('{}'.format(profiles[i]))
		models.append(model)
		#predicting face
		results= model.predict(face)
		results_models.append(results)
		#confidence list
		if results[1] < 500:
		    confidence = int( 100 * (1 - (results[1])/400) )
		    confidence_models.append(confidence)

	for i in range(len(confidence_models)):		
		if confidence_models[i] > 85:
		    print("location: http://192.168.43.217/index2.html")
		    print()
		               

	print("location: http://192.168.43.217/error.html")
	print()

except:
	print("location: http://192.168.43.217/noface.html")
	print()
