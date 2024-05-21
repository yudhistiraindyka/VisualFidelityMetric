import lpips
from PIL import Image
from torchvision import transforms

def calculate_lpips(img1_path, img2_path):
    # Load LPIPS model
    model = lpips.LPIPS(net='alex')

    # Load and preprocess images
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')

    preprocess = transforms.ToTensor()
    img1_tensor = preprocess(img1).unsqueeze(0)
    img2_tensor = preprocess(img2).unsqueeze(0)

    # Calculate LPIPS score
    lpips_score = model(img1_tensor, img2_tensor).item()
    return lpips_score