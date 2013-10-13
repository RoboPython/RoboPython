import robot
import time

R=robot.Robot()

while True:
	m=R.see(1280,1024)
	if len(m)>0:
		print m[0].distance
		if m[0].distance < 0.3:
			print "Grabbing"
			R.servos[0].angle = 70
			R.servos[1].angle = 130
	
		else:
			print "Too far"

	else:	
		print "Nothing there"
		R.servos[0].angle = 130
		R.servos[1].angle = 50
	