import servo
import motor
import Out
import In
import time
import serial
import random
import os,sys


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
















