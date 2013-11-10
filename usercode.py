import robot
import time

R = robot.Robot()


left = R.motors[0]
right = R.motors[1]
lservo = R.servos[0]
rservo = R.servos[1]
state = "a"


def forwards(speed,delay,comment):
	print comment
	left.speed = -speed
	right.speed = -speed
	time.sleep(delay)	
	left.speed = 0
	right.speed = 0

def backwards(speed,delay,comment):
	print comment
	left.speed = speed
	right.speed = speed
	time.sleep(delay)	
	left.speed = 0
	right.speed = 0

def clockwise(speed,delay,comment):
	print comment
	left.speed = -speed
	right.speed = speed
	time.sleep(delay)	
	left.speed = 0
	right.speed = 0

def anticlockwise(speed,delay,comment):
	print comment
	left.speed = speed
	right.speed = -speed
	time.sleep(delay)	
	left.speed = 0
	right.speed = 0


def open_claw():
	print "opening claw"
	lservo.angle = 70
	rservo.angle = 110

def close_claw():
	print "closing claw"
	lservo.angle = 110
	rservo.angle = 50


while True:
	print "starting now"
	if state == "a":
		markers = R.see(1200,1024,True,500)
		if len(markers) ==0:
			state = "b"

		else:
			state = "c"

	if state == "b":
		clockwise(85,0.4,"turning to look for boxes")
		state = "a"


	if state == "c":
		if markers[0].bearing.y < - 20 or markers[0].bearing.y >20:
			state = "d"
		else:
			state = "e"


	if state == "d":
		if markers[0].bearing.y < -10:
			anticlockwise(85,0.4,"box on the left")
		elif markers[0].bearing.y >10:
			clockwise(85,0.4,"box on the right")
		state = "a"

	if state == "e":
		hunted_token = markers[0].code
		forwards(85,1,"going towards that box")
		state = "f"

	if state == "f":
		markers = R.see(1200,1024,True,500)
		state = "g"

	if state == "g":
		if len(markers) >0:
			if hunted_token == markers[0].code:
				state = "e"
			elif hunted_token != markers[0].code:
				state = "h"
		else:
			state = "h"

	if state == "h":
		open_claw()
		forwards(85,1,"grabbing box")
		close_claw()
		state = "a"















