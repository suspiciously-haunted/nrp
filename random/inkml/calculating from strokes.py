import xml.etree.ElementTree as ET

# Function to calculate the bounding box for a list of strokes
def calculate_bounding_box(strokes):
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for stroke in strokes:
        for point in stroke:
            x, y = point
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    return min_x, max_x, min_y, max_y

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

# calculate bounding box area for each trace ID
bounding_boxes = {}
for trace_id, strokes in strokes_by_trace_id.items():
    min_x, max_x, min_y, max_y = calculate_bounding_box(strokes)
    bbox_area = (max_x - min_x) * (max_y - min_y)
    bounding_boxes[str(trace_id)] = bbox_area

# compare bounding box area with the previous trace ID
trace_ids = sorted(bounding_boxes.keys(), key=lambda x: int(x))
for i, trace_id in enumerate(trace_ids):
    bbox_area = bounding_boxes[trace_id]
    if i > 0:
        prev_trace_id = trace_ids[i - 1]
        prev_bbox_area = bounding_boxes[prev_trace_id]
        if bbox_area < prev_bbox_area*.5:
            print(f"Trace ID {trace_id} is a subscript of Trace ID {prev_trace_id}")
        elif bbox_area*.5 > prev_bbox_area:
            print(f"Trace ID {trace_id} is a superscript of Trace ID {prev_trace_id}")
