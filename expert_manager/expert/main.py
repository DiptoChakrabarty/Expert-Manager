#!/usr/bin/env python
#
# Project: Video Streaming with Flask
# Author: Log0 <im [dot] ckieric [at] gmail [dot] com>
# Date: 2014/12/21
# Website: http://www.chioka.in/
# Description:
# Modified to support streaming out with webcams, and not just raw JPEGs.
# Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
# Credits: http://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.
from flask import Flask, render_template, Response,request
from camera import VideoCamera
import os

app = Flask(__name__)

@app.route('/')
def index():
	camera=VideoCamera()
	frame=camera.get_frame()
	return render_template('index2.html')



@app.route('/signup')
def data():
	camera=VideoCamera()
	frame=camera.create_database()
	return render_template('webserver.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)