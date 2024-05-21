import cv2
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(img1_path, img2_path):
    # Load images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        raise ValueError("One of the images couldn't be loaded.")

    # Convert images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    ssim_value, _ = ssim(img1, img2, full=True)
    return ssim_value