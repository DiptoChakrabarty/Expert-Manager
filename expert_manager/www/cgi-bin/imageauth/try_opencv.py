#!/usr/bin/python36

def save_in_database():
	pass
import subprocess as sp
import cgi
import os
print("content-type: text/html")
print()

import cv2
class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        cv2.imwrite("/var/www/cgi-bin/imageauth/image.jpg",image)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def create_database(self):
        count=0
        sp.getoutput("sudo mkdir /var/www/cgi-bin/imageauth/newprofile")
        while count!=100:
            count=count+1
            success, image = self.video.read()

            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            cv2.imwrite("/var/www/cgi-bin/imageauth/newprofile/{}.jpg".format(count),image)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

camera=VideoCamera()

image=camera.get_frame()