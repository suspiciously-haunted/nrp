#'/Users/rgsstudent/Desktop/NRP/CROHME23/WebData_CROHME23/train/IMG_rendering/001-equation000.png'
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models.resnet import model_urls

# Define the class labels for classification
class_labels = model_urls["resnet18"]

# Load the pre-trained ResNet-18 model
model = models.resnet18(pretrained=True)

# Define the image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize the image to 224x224
    transforms.ToTensor(),  # Convert the image to a tensor
])

# Specify the path to your image
image_path = '/Users/rgsstudent/Desktop/NRP/CROHME23/WebData_CROHME23/train/IMG_rendering/001-equation000.png'

# Load the image
image = Image.open(image_path)
image = image.convert("RGB")  # Convert the image to RGB format

# Apply the image transformation
image = transform(image).unsqueeze(0)

# Normalize the image
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],  # Mean values for the ImageNet dataset
    std=[0.229, 0.224, 0.225]  # Standard deviation values for the ImageNet dataset
)
image = normalize(image)

# Set the model to evaluation mode
model.eval()

# Perform inference
with torch.no_grad():
    outputs = model(image)

# Get the predicted class
_, predicted = torch.max(outputs, 1)
predicted_class_index = predicted.item()
predicted_class = class_labels[predicted_class_index]

# Print the predicted class
print('Predicted class:', predicted_class)
