import xml.etree.ElementTree as ET

# load the InkML file
inkml_file = '/Users/rgsstudent/Desktop/NRP/CROHME23/WebData_CROHME23/train/INKML/CROHME2019_train/001-equation000.inkml' 
tree = ET.parse(inkml_file)
root = tree.getroot()

# create a dictionary to store strokes for each trace ID
strokes_by_trace_id = {}

# iterate over each trace element and extract the stroke data
for trace in root.findall('.//{http://www.w3.org/2003/InkML}trace'):
    # get the trace ID
    trace_id = trace.attrib['id']
    
    # the stroke data is a space-separated list of (x, y) coordinates
    stroke_data = trace.text.strip()
    # remove commas from stroke_data
    stroke_data = stroke_data.replace(',', '')
    # split the stroke data into individual (x, y) coordinates
    coordinates = [tuple(map(float, stroke_data.split()[i:i+2])) for i in range(0, len(stroke_data.split()), 2)]

    # check if the trace ID is already present in the dictionary
    if trace_id in strokes_by_trace_id:
        # if it's present, append the coordinates to the existing list
        strokes_by_trace_id[trace_id].append(coordinates)
    else:
        # if it's not present, create a new list with the coordinates
        strokes_by_trace_id[trace_id] = [coordinates]

# print the strokes for each trace ID
for trace_id, strokes in strokes_by_trace_id.items():
    print(f"Trace ID: {trace_id}")
    for stroke in strokes:
        print(stroke)
    print()
