import numpy as np
import pydicom
from PIL import Image
import json

# Read the JSON data from the file
with open('appliedArray.json', 'r') as file:
    appliedArrayJson = file.read()

# Convert the JSON string to a Python list
appliedArray = np.array(json.loads(appliedArrayJson), dtype=np.float32)

# Reshape appliedArray to match the shape of rescaled
appliedArray = appliedArray.reshape((512, 512))
# print('appliedArray: ')
# print(appliedArray.shape)
# print(appliedArray)
# print('')


appliedWWWC = appliedArray
# print('rescaled: ')
# print(rescaled.shape)
# print(rescaled)
# print('')
final_image_after_wwwc = np.uint8(appliedWWWC)
img = Image.fromarray(final_image_after_wwwc)
img.save("after-wwwc-z42.png")
