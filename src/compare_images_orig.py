
import torch
import lpips
from PIL import Image
from torchvision import transforms
import sys

def load_image(image_path):
    # Load image using PIL
    img = Image.open(image_path).convert('RGB')
    # Convert image to tensor
    preprocess = transforms.ToTensor()
    img_tensor = preprocess(img).unsqueeze(0)  # Add batch dimension
    return img_tensor

def compare_images(img1_path, img2_path):
    # Load images
    img1_tensor = load_image(img1_path)
    img2_tensor = load_image(img2_path)

    # Load LPIPS model
    model = lpips.LPIPS(net='alex')  # Use 'vgg' for VGG-based model

    # Calculate LPIPS score
    lpips_score = model(img1_tensor, img2_tensor)
    return lpips_score.item()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_images.py <path_to_image1> <path_to_image2>")
        sys.exit(1)

    img1_path = sys.argv[1]
    img2_path = sys.argv[2]

    score = compare_images(img1_path, img2_path)
    print(f"LPIPS Score: {score}")