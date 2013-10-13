import servo
import motor
import Out
import In
import time
import serial
import random
import os,sys
from pykoki import *
from cv2 import *

'''
Created By Adam Ferguson (@robo_python) 2013
In subsequent uses orginal creator must be credited
but released as opensource software
'''




'''
###BOARD CODES###
1-Servos
2-Motors
3-Output - Digital
4-Input - Analog
5-Input - Digital
#################
'''

ser = serial.Serial("/dev/ttyACM0",9600, timeout= 2)

def width_from_code(code):

    if code <= 100:
        code -= 100

    if code <= 27:
        return 0.25 * (10.0/12.0) #0.25 is printed width, inc. white border

    return 0.1 * (10.0/12.0)

class Robot(object):
	def __init__(self):
		global ser
		self.servos = [ servo.Servo(0,0),
				servo.Servo(1,0),
				servo.Servo(2,0),
				servo.Servo(3,0),
				servo.Servo(4,0),
				servo.Servo(5,0),
				servo.Servo(6,0),
				servo.Servo(7,0)]


		self.motors = [	motor.Motor(0,0),
				motor.Motor(1,0),
				motor.Motor(2,0),
				motor.Motor(3,0)]


		self.outputs = [Out.Output(0,0),
				Out.Output(1,0),
				Out.Output(2,0),
				Out.Output(3,0),
				Out.Output(4,0),
				Out.Output(5,0),
				Out.Output(6,0),
				Out.Output(7,0),]


		self.inputs = [ In.Input(0,0),
				In.Input(1,0),
				In.Input(2,0),
				In.Input(3,0),
				In.Input(4,0),
				In.Input(5,0),
				In.Input(6,0),
				In.Input(7,0),
				In.Input(8,0),
				In.Input(9,0),
				In.Input(10,0),
				In.Input(11,0),
				In.Input(12,0),
				In.Input(13,0),
				In.Input(14,0),
				In.Input(15,0)]


		self.a = ser.readline().rstrip()
		while str(self.a) == "":
			self.a = ser.readline().rstrip()

		print "Starting user code"

	def see(self, WIDTH, HEIGHT):

		params = CameraParams(Point2Df(WIDTH/2, HEIGHT/2),
                	      		Point2Df(571, 571),
                      			Point2Di(WIDTH, HEIGHT))
		command = 'raspistill -w '+str(WIDTH) +' -h '+str(HEIGHT)+' -n -t 0 -o /home/pi/test5.jpg'
		os.system(command)
		pic=cv2.cv.LoadImage("/home/pi/test5.jpg",CV_LOAD_IMAGE_GRAYSCALE) 
		k = PyKoki()
		m = k.find_markers_fp(pic,width_from_code,params) #from basic_example.py
		return m
