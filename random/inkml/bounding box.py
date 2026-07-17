# Sample list of coordinate tuples
coordinates = [(1.0066, 5.46535), (1.0066, 5.4645), (1.00617, 5.46322), (1.00617, 5.46237), (1.00575, 5.46152), (1.00575, 5.46109), (1.00575, 5.46152)]

# Initialize min and max values
min_x = float('inf')
max_x = float('-inf')
min_y = float('inf')
max_y = float('-inf')

# Calculate bounding box
for point in coordinates:
    x, y = point
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
   
print(min_x,max_x,min_y,max_y)