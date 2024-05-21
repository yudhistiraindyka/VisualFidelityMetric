import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import psnr_module
import ssim_module
import lpips_module
import winsound

class VideoComparisonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Comparison")
        self.master.geometry("1280x720")

        # Variables to store video folder paths
        self.native_folder = ""
        self.upscaled_folder = ""

        # Create labels for video frames
        self.native_frame_label = tk.Label(master)
        self.native_frame_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.upscaled_frame_label = tk.Label(master)
        self.upscaled_frame_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Buttons for selecting video folders
        self.select_native_button = tk.Button(master, text="Select NativeVideo Folder", command=self.select_native)
        self.select_native_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.select_upscaled_button = tk.Button(master, text="Select UpscaledVideo Folder", command=self.select_upscaled)
        self.select_upscaled_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Compare buttons
        self.compare_psnr_button = tk.Button(master, text="Compare Videos (PSNR)", command=self.compare_psnr)
        self.compare_psnr_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.compare_ssim_button = tk.Button(master, text="Compare Videos (SSIM)", command=self.compare_ssim)
        self.compare_ssim_button.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.compare_lpips_button = tk.Button(master, text="Compare Videos (LPIPS)", command=self.compare_lpips)
        self.compare_lpips_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(master, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Configure grid resizing
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_columnconfigure(2, weight=1)

    def select_native(self):
        native_folder = filedialog.askdirectory()
        if native_folder:
            self.native_folder = native_folder

    def select_upscaled(self):
        upscaled_folder = filedialog.askdirectory()
        if upscaled_folder:
            self.upscaled_folder = upscaled_folder

    def compare_psnr(self):
        try:
            if self.native_folder and self.upscaled_folder:
                psnr_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="psnr")
                self.display_results(psnr_values, "PSNR")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_ssim(self):
        try:
            if self.native_folder and self.upscaled_folder:
                ssim_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="ssim")
                self.display_results(ssim_values, "SSIM")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_lpips(self):
        try:
            if self.native_folder and self.upscaled_folder:
                lpips_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="lpips")
                self.display_results(lpips_values, "LPIPS")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_videos(self, native_folder, upscaled_folder, metric):
        # Get list of frames in each folder
        native_frames = sorted(os.listdir(native_folder))
        upscaled_frames = sorted(os.listdir(upscaled_folder))

        # Ensure both folders have the same number of frames
        if len(native_frames) != len(upscaled_frames):
            raise ValueError("Number of frames in NativeVideo and UpscaledVideo folders do not match.")

        # Initialize variables to store metric values
        metric_values = []

        # Iterate over frames and calculate metric values
        for native_frame, upscaled_frame in zip(native_frames, upscaled_frames):
            native_frame_path = os.path.join(native_folder, native_frame)
            upscaled_frame_path = os.path.join(upscaled_folder, upscaled_frame)

            if metric == "psnr":
                value = psnr_module.calculate_psnr(native_frame_path, upscaled_frame_path)
            elif metric == "ssim":
                value = ssim_module.calculate_ssim(native_frame_path, upscaled_frame_path)
            elif metric == "lpips":
                value = lpips_module.calculate_lpips(native_frame_path, upscaled_frame_path)

            metric_values.append(value)

        return metric_values

    def display_results(self, metric_values, metric_name):
        # Average the values every 30 frames
        avg_values = [sum(metric_values[i:i + 30]) / 30 for i in range(0, len(metric_values), 30)]

        # Display results
        result_text = f"{metric_name} Values (average values for each second):\n"
        for i, value in enumerate(avg_values):
            result_text += f"Second {i+1}: {value:.4f}\n"
        self.result_label.config(text=result_text)

def main():
    root = tk.Tk()
    app = VideoComparisonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
