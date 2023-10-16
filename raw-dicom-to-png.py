import numpy as np
import pydicom
from PIL import Image

im = pydicom.dcmread("Phantoms\Phantom Test 02\A\Z42")
raw_image = im.pixel_array

final_image_after_wwwc = np.uint8(raw_image)
img = Image.fromarray(final_image_after_wwwc)
img.save("before-wwwc-z42.png")