import natsort
import xml.etree.ElementTree as ET
import os

def extract_labels(inkml_path):
    tree = ET.parse(inkml_path)
    root = tree.getroot()
    prefix = "{http://www.w3.org/2003/InkML}"
    GT_tag = [GT for GT in root.findall(prefix + 'annotation') if GT.attrib == {'type': 'truth'}]
    return GT_tag[0].text

def main():
    test_dir = '/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/val/INKML/CROHME2016_test'
    test_names = [os.path.splitext(name)[0] for name in os.listdir(test_dir) if name.lower().endswith('.inkml')]
    test_names = natsort.natsorted(test_names)

    labels_dict = {}  # Dictionary to store filename-label pairs
    for name in test_names:
        i_name = name + '.inkml'
        test_path = os.path.join(test_dir, i_name)
        label = extract_labels(test_path)
        labels_dict[name] = label

    txt_name = '/Users/rgsstudent/Desktop/NRP/2023/WebData_CROHME23/val/test_2016_caption'
    with open(txt_name, mode='w') as dest_file:
        for filename, label in labels_dict.items():
            dest_file.write(f"{filename}{'   '}{label}\n")

if __name__ == "__main__":
    main()

