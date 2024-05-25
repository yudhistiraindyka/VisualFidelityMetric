# Visual Fidelity Metric

A program made for comparing images and extracting videos using PSNR, SSIM, and LPIPS metrics.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [Extracting Videos](#extracting-videos)
  - [Comparing Images](#comparing-images)
  - [Comparing Videos](#comparing-videos)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Description

Visual Fidelity Metric is a tool designed for comparing images and extracting video frames using three popular metrics:
- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)
- LPIPS (Learned Perceptual Image Patch Similarity)

This tool helps in assessing the quality and fidelity of images and videos by providing quantitative comparisons through a user-friendly GUI.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have the following software installed:
- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Git](https://git-scm.com/)

### Clone the Repository

First, clone the repository to your local machine:
```sh
git clone https://github.com/yudhistiraindyka/VisualFidelityMetric.git
cd VisualFidelityMetric
```
### Set up Virtual Environment

#### On Windows
```
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

## Usage

### Extracting Videos

To extract each frame from a video, use the following command:
```
python src/video_extract.py
```
This will open the GUI for frame extraction program.

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/e25b2b5e-846a-49fa-bf7f-c2de71ed3306" alt="Example Image" width="400" />
</p>

1. Click browse, then navigate to the video that want to be extracted, click ok
2. Click extract frames, then choose the output folder (preferably separate folders for native and upscaled)
3. The progress should appear and we can wait until it finishes

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/c8bfb5bf-aef5-4459-8197-f86283e74f8e" alt="Example Image" width="400" />
</p>


### Comparing images

To compare two images using the provided metrics, use the following command:
```
python src/main_app.py
```
This will open the GUI for image comparison.

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/a9efccd4-0ee5-446a-aca2-7e449f3fc180" alt="Example Image" width="800" />
</p>

1. Click on the "Select First Image (Native)" and choose the native image
2. Click on the "Select Second Image (Upscaled)" and choose the upscaled image

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/7f8f1cca-059c-4018-b7d4-0d94dada61c6" alt="Example Image" width="800" />
</p>

3. Click on the comparison method that you want (PSNR, SSIM, LPIPS)
4. The result should appear

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/8bd817e4-4a4f-4b48-b165-490b6b2cec05" alt="Example Image" width="800" />
</p>

### Comparing videos

To compare videos, make sure the videos are extracted to images first, one in a folder for native, another one in a folder for upscaled, and make sure <i><b> the number of images are the same.</b></i>
After making sure we've extracted the video, use the following command:
```
python src/compare_videos_interval.py
```
This will open the GUI for video comparison.
<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/72e1a1ee-64b1-4d04-aa8d-e1a7bc1e6e97" alt="Example Image" width="800" />
</p>

1. Click "Select native video folder" and click on the folder which contains native images
2. Click "Select upscaled video folder" and click on the folder which contains native images
3. Chose the sampling interval (if the video is in 30 fps, 2 means only 2 sample are taken each second, the 15th and the 30th frame)
4. Click on the comparison method that we want, wait till it finishes (might take minutes) and the result should appear
5. The result will provide the average values of (PSNR, SSIM, or LPIPS) for each second

<p align="center">
  <img src="https://github.com/yudhistiraindyka/VisualFidelityMetric/assets/33085123/fffd8997-5342-4d99-9ddd-38fe6b0777e9" alt="Example Image" width="800" />
</p>

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/yudhistiraindyka/VisualFidelityMetric/blob/master/LICENSE) file for details.

## Contact
For any questions or suggestions, please contact:

Yudhistira Indyka - yudhistira.indyka@protonmail.com

## Acknowledgements
- Special thanks to the engineers that came up with PSNR, SSIM, and LPIPS method for image comparison.
- Thanks to VSCode, NumPy, PyTorch, and Python for providing a thorough documentation.
