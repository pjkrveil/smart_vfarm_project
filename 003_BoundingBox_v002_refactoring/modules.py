# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import imutils

# load the image
def load_img(filename):
	image = cv2.imread(filename)

	return image

# convert image to grayscale, and blur it
def blurring(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)

	return blurred

# threshold the image to reveal light regions in the blurred image
def threshold(blurred):
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

	# perform a series of erosions and dilations to remove
	# any small blobs of noise from the thresholded image
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=4)

	return thresh


def masking(thresh):
	# perform a connected component analysis on the thresholded image,
	# then initialize a mask to store only the "large" components
	labels = measure.label(thresh, neighbors=8, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")

	return labels, mask

def 

