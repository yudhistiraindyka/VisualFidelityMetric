import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os

class VideoFrameExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Frame Extractor")
        self.master.geometry("400x200")

        # Variables to store video path
        self.video_path = ""

        # Create label for video path
        self.video_path_label = tk.Label(master, text="Video Path: ")
        self.video_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.video_path_var = tk.StringVar()
        self.video_path_entry = tk.Entry(master, textvariable=self.video_path_var, state="readonly", width=30)
        self.video_path_entry.grid(row=0, column=1, padx=5, pady=5)

        # Browse button
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_video, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        # Extract frames button
        self.extract_frames_button = tk.Button(master, text="Extract Frames", command=self.extract_frames)
        self.extract_frames_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Progress label
        self.progress_label = tk.Label(master, text="Frames extracted: 0")
        self.progress_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def browse_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if video_path:
            self.video_path = video_path
            self.video_path_var.set(video_path)

    def extract_frames(self):
        if not self.video_path:
            messagebox.showerror("Error", "Please select a video file.")
            return

        output_folder = filedialog.askdirectory()
        if not output_folder:
            return

        # Open the video file
        video = cv2.VideoCapture(self.video_path)
        
        # Check if the video opened successfully
        if not video.isOpened():
            messagebox.showerror("Error", "Could not open video.")
            return

        # Get some properties of the video
        fps = int(video.get(cv2.CAP_PROP_FPS))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Loop through each frame and extract it
        current_frame = 0
        while True:
            ret, frame = video.read()

            if not ret:
                break

            # Save frame
            frame_path = os.path.join(output_folder, f"frame_{current_frame}.jpg")
            cv2.imwrite(frame_path, frame)

            # Update progress label
            self.progress_label.config(text=f"Frames extracted: {current_frame + 1}/{total_frames}")
            self.master.update_idletasks()

            current_frame += 1

        # Release video object
        video.release()
        messagebox.showinfo("Information", "Frame extraction complete.")

def main():
    root = tk.Tk()
    app = VideoFrameExtractorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
