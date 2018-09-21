# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2

class Modules():
	def __init__(self):
		pass

	def load_img(self, filename):
		""" Load the image with filename """
		image = cv2.imread(filename)

		return image

	def blurring(self, image):
		""" Convert image to grayscale, and blur it """
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (11, 11), 0)

		return blurred


	def threshold(self, blurred, l_range, h_range):
		""" Threshold the image to reveal light regions in the blurred image """
		thresh = cv2.threshold(blurred, l_range, h_range, cv2.THRESH_BINARY)[1]

		# perform a series of erosions and dilations to remove
		# any small blobs of noise from the thresholded image
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=4)

		return thresh


	def masking(self, thresh):
		""" Perform a connected component analysis on the thresholded image,
			then initialize a mask to store only the "large" components
		"""
		labels = measure.label(thresh, neighbors=8, background=0)
		mask = np.zeros(thresh.shape, dtype="uint8")

		# loop over the unique components
		for label in np.unique(labels):
			# if this is the background label, ignore it
			if label == 0:
				continue

			# otherwise, construct the label mask and count the
			# number of pixels 
			labelMask = np.zeros(thresh.shape, dtype="uint8")
			labelMask[labels == label] = 255
			numPixels = cv2.countNonZero(labelMask)

			# if the number of pixels in the component is sufficiently
			# large, then add it to our mask of "large blobs"
			if numPixels > 300:
				mask = cv2.add(mask, labelMask)

		return mask


	def preProcessing(self, image, l_range, h_range):
		""" Wrapping function for preprocessing process with setting low and high ranges for a mask image """
		blurred = self.blurring(image)
		thres = self.threshold(blurred, l_range, h_range)
		mask = self.masking(thres)

		return mask


	def find_contour(self, mask, image):
		""" Find the contours in the mask, then sort them from left to right """
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
		cnts = contours.sort_contours(cnts)[0]

		lc_list = []

		for (i, c) in enumerate(cnts):
			# draw the bright spot on the image
			(x, y, w, h) = cv2.boundingRect(c)

			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

			cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

			lc_list.append((x, y, w, h))

		return lc_list

	def point_ctr(self, location_list, image):
		""" Pointing the center point of bounding boxes """
		ctr_list = []

		for (x, y, w, h) in location_list:
			(cX, cY) = (x + w // 2, y + h // 2)
			# ((cX, cY), radius) = cv2.minEnclosingCircle(c)
			cv2.circle(image, (int(cX), int(cY)), 2, (0, 0, 255), 2)

			ctr_list.append((cX, cY))

		return ctr_list, image

	def save_lcdata(self, ctr_list, filename):
		""" Save the cooridnate of the center point of bounding boxes """
		file = open(filename, 'w')

		f_line = "num\tcX\tcY\n"
		file.write(f_line)
		num = 1

		for (cX, cY) in ctr_list:
			data = "%d\t%d\t%d\n" % (num, cX, cY)
			file.write(data)
			num += 1

		file.close()

	def extract_data(self, location_list, image, filename):
		""" Wrapping fucntion for finding the center location of bounding boxes
			and save each coordinate data as text file
		"""
		ctr_list, image = self.point_ctr(location_list, image)
		self.save_lcdata(ctr_list, filename)

		return image

	def show_img(self, image):
		# show the output image
		cv2.imshow("Image", image)
		cv2.waitKey(0)