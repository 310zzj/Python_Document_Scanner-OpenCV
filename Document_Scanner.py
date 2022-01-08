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
		-------
		None
		"""
		
		self.img = img
		
	def Resize_Image(self, final_height, img):
		"""
		Resizes the image by preserving its axis ratio. 

		An argument 'img' can be either a string or an image array itself.

		Parameters
		----------
		img : str/array
			image name (image array) of the document/photo
		final_height : int 
			final height to resize an image to (in pixels)

		Returns
		-------
		Resized image (array)
		"""

		if isinstance(img, str):
			print("This is string!")
			img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
		else:
			print("This is not string!")
			print(type(img))
			img = img
		# Optional - resizing an image by preserving its aspect ratio
		# percentage by which we resize our image (based on the hight)
		height_ratio = final_height / img.shape[0]
		#calculate the ratio of original dimensions
		height, width = int(img.shape[0] * height_ratio), int(img.shape[1] * hei