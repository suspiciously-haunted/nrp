import os
import pickle
from PIL import Image

# Path to the folder containing PNG images
image_folder = '/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/val/IMG_rendering'

# Create a dictionary to store the image data
image_data = {}

# Iterate over the PNG files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.png'):
        image_path = os.path.join(image_folder, filename)
        with Image.open(image_path) as img:
            image_data[filename] = img.convert('RGB')

# Specify the output Pickle file
output_pickle_file = '/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/val/IMG_rendering.pkl'

# Write the image data dictionary to the Pickle file
with open(output_pickle_file, 'wb') as f:
    pickle.dump(image_data, f)

print(f"Image data from '{image_folder}' converted and saved to '{output_pickle_file}'.")

