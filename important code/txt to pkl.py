import pickle

# Read the text content from the input file
input_file = "/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/train/val_2019 (spaced).txt"
with open(input_file, 'r', encoding='utf-8') as f:
    text_content = f.read()

# Specify the output Pickle file
output_pickle_file = "/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/train/val_2019 (spaced).pkl"

# Create a dictionary to store the text content
data = {'text': text_content}

# Write the dictionary to the Pickle file
with open(output_pickle_file, 'wb') as f:
    pickle.dump(data, f)

print(f"Text data from '{input_file}' converted and saved to '{output_pickle_file}'.")

