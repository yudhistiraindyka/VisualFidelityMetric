import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import psnr_module
import ssim_module
import lpips_module
import winsound

class ImageComparisonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Comparison")
        self.master.geometry("800x500")

        # Variables to store image paths
        self.img1_path = ""
        self.img2_path = ""

        # Create labels for images
        self.img1_label = tk.Label(master)
        self.img1_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.img2_label = tk.Label(master)
        self.img2_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Buttons for selecting images
        self.select_img1_button = tk.Button(master, text="Select First Image (Native)", command=self.select_img1, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.select_img1_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.select_img2_button = tk.Button(master, text="Select Second Image (Upscaled)", command=self.select_img2, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.select_img2_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Compare buttons
        self.compare_psnr_button = tk.Button(master, text="Compare Images (PSNR)", command=self.compare_psnr, bg="#A9A9A9", fg="white", font=("Arial", 10))
        self.compare_psnr_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.compare_ssim_button = tk.Button(master, text="Compare Images (SSIM)", command=self.compare_ssim, bg="#A9A9A9", fg="white", font=("Arial", 10))
        self.compare_ssim_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.compare_lpips_button = tk.Button(master, text="Compare Images (LPIPS)", command=self.compare_lpips, bg="#A9A9A9", fg="white", font=("Arial", 10))
        self.compare_lpips_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Result label
        self.result_label = tk.Label(master, text="Result: ", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")


        # Configure grid resizing
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.master.grid_columnconfigure(i, weight=1)

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

    def compare_psnr(self):
        try:
            if self.img1_path and self.img2_path:
                psnr_value = psnr_module.calculate_psnr(self.img1_path, self.img2_path)
                self.result_label.config(text=f"PSNR Value: {psnr_value:.6f}")
                winsound.MessageBeep()  # Play Windows alert sound
            else:
                messagebox.showerror("Error", "Please select both images.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_ssim(self):
        try:
            if self.img1_path and self.img2_path:
                ssim_value = ssim_module.calculate_ssim(self.img1_path, self.img2_path)
                self.result_label.config(text=f"SSIM Value: {ssim_value:.6f}")
                winsound.MessageBeep()  # Play Windows alert sound
            else:
                messagebox.showerror("Error", "Please select both images.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_lpips(self):
        try:
            if self.img1_path and self.img2_path:
                lpips_value = lpips_module.calculate_lpips(self.img1_path, self.img2_path)
                self.result_label.config(text=f"LPIPS Value: {lpips_value:.6f}")
                winsound.MessageBeep()  # Play Windows alert sound
            else:
                messagebox.showerror("Error", "Please select both images.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_image(self, image_path, label):
        try:
            # Load image
            img = Image.open(image_path)
            img.thumbnail((int(self.master.winfo_width() / 2) - 10, self.master.winfo_height() - 150))  # Resize image to fit half of the window
            img_tk = ImageTk.PhotoImage(img)

            # Display image
            label.configure(image=img_tk)
            label.image = img_tk  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while displaying the image: {e}")

def main():
    root = tk.Tk()
    app = ImageComparisonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
