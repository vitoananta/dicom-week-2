import numpy as np
import pydicom
from PIL import Image
import json

# Read JSON file
with open('appliedArray.json', 'r') as file:
    appliedArray = json.load(file)

# Convert the list to a NumPy array
appliedArray = np.array(appliedArray, dtype=np.float32)
print(appliedArray)
print(type(appliedArray))

# Reshape the array if needed based on your original shape
# For example, if the shape is (slice, rows, cols), you can do:
# appliedArray = appliedArray.reshape((slice, rows, cols))

# Your existing code
im = pydicom.dcmread("Phantoms\Phantom Test 02\A\Z21")
new_image = im.pixel_array

rescaled = appliedArray
print(rescaled)
print(type(rescaled))
final_image = np.uint8(rescaled)

img = Image.fromarray(final_image)
img.show()
img.save("test.png")
