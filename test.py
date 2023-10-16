import numpy as np
from PIL import Image
import csv

# Read the CSV file
with open('appliedArray.csv', 'r') as file:
    csv_data = file.read()

# Convert the CSV data to a NumPy array
applied_array = np.array([float(value) for value in csv_data.split(',')])

# Reshape the array to match the shape used in JavaScript
applied_array = applied_array.reshape(shape['slice'], shape['rows'], shape['cols'])

# Convert to uint8
final_image = np.uint8(applied_array)

# Create an image
img = Image.fromarray(final_image)

# Display and save the image
img.show()
img.save("test.png")
print(type(final_image))
