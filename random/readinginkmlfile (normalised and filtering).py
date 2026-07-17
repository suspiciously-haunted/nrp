import xml.etree.ElementTree as ET
import numpy as np

# load the InkML file
inkml_file = '/Users/rgsstudent/Desktop/NRP/inkml/2012'
tree = ET.parse(inkml_file)
root = tree.getroot()

# iterate over each trace element and extract the stroke data
strokes = []
for trace in root.findall('.//{http://www.w3.org/2003/InkML}trace'):
    # the stroke data is a space-separated list of (x, y) coordinates
    stroke_data = trace.text.strip()
    # remove commas from stroke_data
    stroke_data = stroke_data.replace(',', '')
    # split the stroke data into individual (x, y) coordinates
    coordinates = [tuple(map(float, point.split())) for point in stroke_data.split()]
    # do something with the stroke data, e.g., store it in a list of strokes
    strokes.append(coordinates)

# convert strokes to a numpy array
strokes_array = np.array(strokes)

# normalize the strokes to a target width and height
target_width = 100.0
target_height = 100.0

normalized_strokes = []
for stroke in strokes_array:
    x_coords = stroke[:, 0]
    y_coords = stroke[:, 1]
    min_x, max_x = np.min(x_coords), np.max(x_coords)
    min_y, max_y = np.min(y_coords), np.max(y_coords)
    width = max_x - min_x
    height = max_y - min_y

    x_scale = target_width / width
    y_scale = target_height / height

    normalized_stroke = np.array([(x - min_x) * x_scale, (y - min_y) * y_scale] for x, y in stroke)
    normalized_strokes.append(normalized_stroke)

# print the normalized strokes
print(normalized_strokes)
