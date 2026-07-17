import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# load the InkML file
inkml_file = '/Users/rgsstudent/Desktop/NRP/CROHME23/WebData_CROHME23/train/INKML/CROHME2019_train/001-equation000.inkml'
tree = ET.parse(inkml_file)
root = tree.getroot()

# iterate over each trace element and extract the stroke data
for trace in root.findall('.//{http://www.w3.org/2003/InkML}trace'):
    # the stroke data is a space-separated list of (x, y) coordinates
    stroke_data = trace.text.strip()
    # remove commas from stroke_data
    stroke_data = stroke_data.replace(',', '')
    # split the stroke data into individual (x, y) coordinates
    coordinates = [tuple(map(float, stroke_data.split()[i:i+2])) for i in range(0, len(stroke_data.split()), 2)]

    # extract x and y coordinates separately
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]

    # plot the stroke
    plt.plot(x, y)
    

# configure the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('InkML Strokes')
plt.axis('equal')  # equal scaling for x and y axes
plt.gca().invert_yaxis()
plt.show()
