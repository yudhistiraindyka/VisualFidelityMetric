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

        # Variable to store the selected frames per second for sampling
        self.frames_per_second = tk.IntVar(value=5)  # Default value is 5 frames per second

        # Create labels for video frames
        self.native_frame_label = tk.Label(master)
        self.native_frame_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.upscaled_frame_label = tk.Label(master)
        self.upscaled_frame_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Buttons for selecting video folders
        self.select_native_button = tk.Button(master, text="Select Native Video Folder", command=self.select_native)
        self.select_native_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.select_upscaled_button = tk.Button(master, text="Select Upscaled Video Folder", command=self.select_upscaled)
        self.select_upscaled_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # OptionMenu for selecting frames per second for sampling
        self.fps_label = tk.Label(master, text="Frames per second for sampling:")
        self.fps_label.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.fps_menu = tk.OptionMenu(master, self.frames_per_second, 2, 5, 10, 15, 30)
        self.fps_menu.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Compare buttons
        self.compare_psnr_button = tk.Button(master, text="Compare Videos (PSNR)", command=self.compare_psnr)
        self.compare_psnr_button.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.compare_ssim_button = tk.Button(master, text="Compare Videos (SSIM)", command=self.compare_ssim)
        self.compare_ssim_button.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.compare_lpips_button = tk.Button(master, text="Compare Videos (LPIPS)", command=self.compare_lpips)
        self.compare_lpips_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(master, text="Result: ")
        self.result_label.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

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
                fps = self.frames_per_second.get()
                psnr_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="psnr", frames_per_second=fps)
                self.display_results(psnr_values, "PSNR")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_ssim(self):
        try:
            if self.native_folder and self.upscaled_folder:
                fps = self.frames_per_second.get()
                ssim_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="ssim", frames_per_second=fps)
                self.display_results(ssim_values, "SSIM")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_lpips(self):
        try:
            if self.native_folder and self.upscaled_folder:
                fps = self.frames_per_second.get()
                lpips_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="lpips", frames_per_second=fps)
                self.display_results(lpips_values, "LPIPS")
                winsound.MessageBeep()  # Play default alert sound
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_videos(self, native_folder, upscaled_folder, metric, frames_per_second):
        # Get list of frames in each folder
        native_frames = sorted(os.listdir(native_folder))
        upscaled_frames = sorted(os.listdir(upscaled_folder))

        # Ensure both folders have the same number of frames
        if len(native_frames) != len(upscaled_frames):
            raise ValueError("Number of frames in Native Video and Upscaled Video folders do not match.")

        # Determine the sampling interval
        frame_rate = 30  # Assuming 30 FPS
        sampling_interval = frame_rate // frames_per_second

        # Initialize variables to store metric values
        metric_values = []

        # Iterate over frames with the specified sampling interval and calculate metric values
        for i in range(0, len(native_frames), sampling_interval):
            native_frame_path = os.path.join(native_folder, native_frames[i])
            upscaled_frame_path = os.path.join(upscaled_folder, upscaled_frames[i])

            if metric == "psnr":
                value = psnr_module.calculate_psnr(native_frame_path, upscaled_frame_path)
            elif metric == "ssim":
                value = ssim_module.calculate_ssim(native_frame_path, upscaled_frame_path)
            elif metric == "lpips":
                value = lpips_module.calculate_lpips(native_frame_path, upscaled_frame_path)

            metric_values.append(value)

        return metric_values

    def display_results(self, metric_values, metric_name):
        # Calculate the average of the metric values for each second
        frames_per_second = self.frames_per_second.get()
        frames_per_interval = frames_per_second

        avg_values_per_second = []
        num_intervals = len(metric_values) // frames_per_interval

        for i in range(num_intervals):
            start_index = i * frames_per_interval
            end_index = start_index + frames_per_interval
            avg_value = sum(metric_values[start_index:end_index]) / frames_per_interval
            avg_values_per_second.append(avg_value)

        # Display results
        result_text = f"{metric_name} Values (average values for each second):\n"
        for i, value in enumerate(avg_values_per_second):
            result_text += f"Second {i+1}: {value:.4f}\n"
        self.result_label.config(text=result_text)

def main():
    root = tk.Tk()
    app = VideoComparisonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
