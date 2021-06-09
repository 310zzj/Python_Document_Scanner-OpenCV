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
		Transforms th