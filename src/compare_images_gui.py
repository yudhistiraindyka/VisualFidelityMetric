import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import lpips
from torchvision import transforms

class ImageComparerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Comparer")
        self.master.geometry("1280x720")

        # Variables to store image paths
        self.img1_path = ""
        self.img2_path = ""

        # Create labels for images
        self.img1_label = tk.Label(master)
        self.img1_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.img2_label = tk.Label(master)
        self.img2_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Buttons for selecting images
        self.select_img1_button = tk.Button(master, text="Select First Image", command=self.select_img1)
        self.select_img1_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.select_img2_button = tk.Button(master, text="Select Second Image", command=self.select_img2)
        self.select_img2_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Compare button
        self.compare_button = tk.Button(master, text="Compare Images", command=self.compare_images)
        self.compare_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(master, text="LPIPS Score: ")
        self.result_label.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Configure grid resizing
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_columnconfigure(2, weight=1)

    def select_img1(self):
        img1_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if img1_path:
            self.img1_path = img1_path
            self.display_image(self.img1_path, self.img1_label)

    def select_img2(self):
        img2_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if img2_path:
            self.img2_path = img2_path
            self.display_image(self.img2_path, self.img2_label)

    def compare_images(self):
        if self.img1_path and self.img2_path:
            # Load images
            img1_tensor = self.load_image(self.img1_path)
            img2_tensor = self.load_image(self.img2_path)

            # Load LPIPS model
            model = lpips.LPIPS(net='alex')

            # Calculate LPIPS score
            lpips_score = model(img1_tensor, img2_tensor).item()
            self.result_label.config(text=f"LPIPS Score: {lpips_score:.4f}")

    def load_image(self, image_path):
        # Load image using PIL
        img = Image.open(image_path).convert('RGB')
        # Convert image to tensor
        preprocess = transforms.ToTensor()
        img_tensor = preprocess(img).unsqueeze(0)  # Add batch dimension
        return img_tensor

    def display_image(self, image_path, label):
        # Load image
        img = Image.open(image_path)
        img.thumbnail((int(self.master.winfo_width() / 2) - 10, self.master.winfo_height() - 100))  # Resize image to fit half of the window
        img_tk = ImageTk.PhotoImage(img)

        # Display image
        label.configure(image=img_tk)
        label.image = img_tk  # Keep a reference to prevent garbage collection

def main():
    root = tk.Tk()
    app = ImageComparerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
