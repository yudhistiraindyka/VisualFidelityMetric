import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import time
import psnr_module
import ssim_module
import lpips_module
import winsound

class VideoComparisonApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Comparison")
        self.master.geometry("800x850")

        # Variables to store video folder paths
        self.native_folder = ""
        self.upscaled_folder = ""

        # Variable to store the selected frames per second for sampling
        self.frames_per_second = tk.IntVar(value=5)

        # Frame for video selection buttons
        self.video_frame = tk.Frame(master)
        self.video_frame.pack(pady=10)

        # Buttons for selecting video folders
        self.select_native_button = tk.Button(self.video_frame, text="Select Native Video Folder", command=self.select_native, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.select_native_button.pack(side=tk.LEFT, padx=5)
        self.select_upscaled_button = tk.Button(self.video_frame, text="Select Upscaled Video Folder", command=self.select_upscaled, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.select_upscaled_button.pack(side=tk.LEFT, padx=5)

        # Frame for FPS selection
        self.fps_frame = tk.Frame(master)
        self.fps_frame.pack(pady=10)

        # OptionMenu for selecting frames per second for sampling
        self.fps_label = tk.Label(self.fps_frame, text="Frames per second for sampling:")
        self.fps_label.pack(side=tk.LEFT, padx=5)
        self.fps_menu = tk.OptionMenu(self.fps_frame, self.frames_per_second, 2, 5, 10, 15, 30, 60)
        self.fps_menu.pack(side=tk.LEFT, padx=5)

        # Frame for comparison buttons
        self.compare_frame = tk.Frame(master)
        self.compare_frame.pack(pady=10)

        # Compare buttons
        self.compare_psnr_button = tk.Button(self.compare_frame, text="Compare Videos (PSNR)", command=self.compare_psnr)
        self.compare_psnr_button.pack(side=tk.LEFT, padx=5)
        self.compare_ssim_button = tk.Button(self.compare_frame, text="Compare Videos (SSIM)", command=self.compare_ssim)
        self.compare_ssim_button.pack(side=tk.LEFT, padx=5)
        self.compare_lpips_button = tk.Button(self.compare_frame, text="Compare Videos (LPIPS)", command=self.compare_lpips)
        self.compare_lpips_button.pack(side=tk.LEFT, padx=5)

        # Result label
        self.result_label = tk.Label(master, text="Result: ", wraplength=700, font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        # Save button (initially hidden)
        self.save_button = tk.Button(master, text="Save Results", command=self.save_results, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.save_button.pack(pady=10)
        self.save_button.pack_forget()

        self.metric_values = []
        self.metric_name = ""
        self.elapsed_time = 0

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
                start_time = time.time()
                psnr_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="psnr", frames_per_second=fps)
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.display_results(psnr_values, "PSNR", elapsed_time)
                winsound.MessageBeep()
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_ssim(self):
        try:
            if self.native_folder and self.upscaled_folder:
                fps = self.frames_per_second.get()
                start_time = time.time()
                ssim_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="ssim", frames_per_second=fps)
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.display_results(ssim_values, "SSIM", elapsed_time)
                winsound.MessageBeep()
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_lpips(self):
        try:
            if self.native_folder and self.upscaled_folder:
                fps = self.frames_per_second.get()
                start_time = time.time()
                lpips_values = self.compare_videos(self.native_folder, self.upscaled_folder, metric="lpips", frames_per_second=fps)
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.display_results(lpips_values, "LPIPS", elapsed_time)
                winsound.MessageBeep()
            else:
                messagebox.showerror("Error", "Please select both video folders.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def compare_videos(self, native_folder, upscaled_folder, metric, frames_per_second):
        native_frames = sorted(os.listdir(native_folder))
        upscaled_frames = sorted(os.listdir(upscaled_folder))

        if len(native_frames) != len(upscaled_frames):
            raise ValueError("Number of frames in Native Video and Upscaled Video folders do not match.")

        total_frames = len(native_frames)
        duration = 30  # Duration in seconds
        frame_rate = total_frames // duration

        sampling_interval = frame_rate // frames_per_second

        metric_values = []

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

        self.metric_values = metric_values
        self.metric_name = metric
        return metric_values

    def display_results(self, metric_values, metric_name, elapsed_time):
        frames_per_second = self.frames_per_second.get()
        frames_per_interval = frames_per_second

        avg_values_per_second = []
        num_intervals = len(metric_values) // frames_per_interval

        for i in range(num_intervals):
            start_index = i * frames_per_interval
            end_index = start_index + frames_per_interval
            avg_value = sum(metric_values[start_index:end_index]) / frames_per_interval
            avg_values_per_second.append(avg_value)

        result_text = f"{metric_name} Values (average values for each second):\n"
        for i, value in enumerate(avg_values_per_second):
            result_text += f"Second {i+1}: {value:.4f}\n"
        result_text += f"\nTime taken: {elapsed_time:.2f} seconds"
        self.result_label.config(text=result_text)

        self.elapsed_time = elapsed_time

        # Show the save button
        self.save_button.pack()

    def save_results(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV file", "*.csv"), ("Text file", "*.txt")])
        if save_path:
            with open(save_path, 'w') as file:
                frames_per_second = self.frames_per_second.get()
                frames_per_interval = frames_per_second

                avg_values_per_second = []
                num_intervals = len(self.metric_values) // frames_per_interval

                for i in range(num_intervals):
                    start_index = i * frames_per_interval
                    end_index = start_index + frames_per_interval
                    avg_value = sum(self.metric_values[start_index:end_index]) / frames_per_interval
                    avg_values_per_second.append(avg_value)

                file.write(f"{self.metric_name.upper()} Values (average values for each second):\n")
                for i, value in enumerate(avg_values_per_second):
                    file.write(f"Second {i+1}, {value:.4f}\n")
                file.write(f"\nTime taken: {self.elapsed_time:.2f} seconds")


def main():
    root = tk.Tk()
    app = VideoComparisonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
