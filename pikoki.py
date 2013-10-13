from pykoki import *
from cv2 import *


def width_from_code(code):

    if code <= 100:
        code -= 100

    if code <= 27:
        return 0.25 * (10.0/12.0) #0.25 is printed width, inc. white border

    return 0.1 * (10.0/12.0)

def see(WIDTH, HEIGHT):

	params = CameraParams(Point2Df(WIDTH/2, HEIGHT/2),
                      		Point2Df(571, 571),
                      		Point2Di(WIDTH, HEIGHT))

	print "start"
	command = 'raspistill -w '+WIDTH +' -h '+HEIGHT+' -n -t 0 -o /home/pi/test5.jpg'
	os.system(command)
	pic=cv2.cv.LoadImage("/home/pi/test5.jpg",CV_LOAD_IMAGE_GRAYSCALE) 

	k = PyKoki()
	print "trying"
	m = k.find_markers_fp(pic,width_from_code,params) #from basic_example.py
	if len(m)== 0:
    		print "Nothing there"
	else:
    		print m
