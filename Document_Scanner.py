import numpy as np
import cv2
from skimage.filters import threshold_local
import math
from scipy import ndimage
print("Imports are Done!")


class Scanner:
	"""
	A class to scan (and perform related operations on) a document.

	...

	Attributes
	----------
	img : str
		image name of the document/photo.

	Methods
	-------
	Resize_Image(final_height, img):
		Resizes the image by preserving its axis ratio.

	Scan_View():
		Transforms the image/document view into B&W (proper scanned colour scheme).

	Rotation():
		Automatically rotates the image/document to a straight (top-down, face-on) view.

	"""

	def __init__(self, img):
		"""
		Constructs all the necessary attributes for the person object.

		Parameters
		----------
		img : str
			image name of the document/photo

		Returns