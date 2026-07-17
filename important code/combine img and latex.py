import os
import pickle

# Specify the paths to the image folder and text files folder
image_folder = '/Users/rgsstudent/Desktop/actual codes/SAN/data/off_image_train/'
text_file = '/Users/rgsstudent/Desktop/actual codes/SAN/data/train_caption.txt'
output_file = '/Users/rgsstudent/Desktop/train_dictionary.pkl'

# Get the list of image filenames (excluding file extensions)
image_filenames = [os.path.splitext(filename)[0] for filename in os.listdir(image_folder) if filename.endswith('.bmp')]

# Create a dictionary to store combined data
combined_data = {}

# Iterate through the text files folder
for filename in os.listdir(text_folder):
    if filename.endswith('.txt'):
        text_file_path = os.path.join(text_folder, filename)
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            text_content = text_file.read().strip()
        
        # Extract the numeric part from the text file name
        numeric_part = filename.split('_')[0]
        
        # Check if the numeric part corresponds to an image filename
        if numeric_part in image_filenames:
            combined_data[int(numeric_part)] = text_content

# Write the combined data to the output file
with open(output_file, 'w', encoding='utf-8') as output:
    for key in sorted(combined_data.keys()):
        output.write(f'{key}_em_0\t{combined_data[key]}\n')

with open(output_file, 'wb') as output_pickle:
    pickle.dump(combined_data, output_pickle)

print(f"Combined data written to {output_file}")

